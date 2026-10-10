#!/usr/bin/env python3
"""
send_tchap.py — Envoie le résumé de la note de veille du jour dans un salon Tchap.

Changements par rapport à la version précédente (10/10/2026) :
  * mise en forme : le message est écrit en Markdown (# titre, ## section,
    puces) et part accompagné de sa version HTML (formatted_body). C'est elle
    que Tchap affiche : il n'interprète pas le Markdown d'un message reçu ;
  * contenu : seule la section « Résumé » est reprise. « À retenir » ne l'est plus.

Garanties :
  * taille stable   : la troncature est faite ici, jamais par le modèle ;
  * pas de doublon  : une note déjà envoyée n'est pas renvoyée ;
  * statut fiable   : la réponse Matrix est vérifiée, l'event_id journalisé ;
  * sortie silencieuse : sync filtré, donc pas de bruit de déchiffrement E2E.

Dernière ligne de sortie, toujours parsable :
    TCHAP_RESULT=sent|already_sent|dry_run|failed [event_id=...] chars=N

Sortie : 0 = envoyé ou déjà envoyé · 1 = échec.

Env : TCHAP_HOMESERVER, TCHAP_USERNAME, TCHAP_PASSWORD, TCHAP_ROOM_ID
      TCHAP_STORE (défaut .tchap_store), REPO_BASE_URL (optionnel)

Usage :
    python scripts/send_tchap.py --note veilles/2026-09-01.md [--dry-run]

Dépendances : voir scripts/setup_tchap.sh
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import logging
import os
import re
import sys
from html import escape
from pathlib import Path

MAX_CHARS = 3500
ENV_VARS = ("TCHAP_HOMESERVER", "TCHAP_USERNAME", "TCHAP_PASSWORD", "TCHAP_ROOM_ID")
STORE = Path(os.environ.get("TCHAP_STORE", ".tchap_store"))
REPO_BASE = os.environ.get(
    "REPO_BASE_URL", "https://github.com/DGE-SEN-DPIA/DPIA_veille/blob/main"
)

# Sections de la note reprises dans le message (sous-chaînes, en minuscules).
KEEP_SECTIONS = ("résum", "resum")

# Sync minimal : aucun événement de timeline, donc aucun déchiffrement tenté.
SYNC_FILTER = {
    "room": {
        "timeline": {"limit": 0},
        "state": {"lazy_load_members": True},
        "ephemeral": {"types": []},
    },
    "presence": {"types": []},
}


def build_message(md_text: str, note_name: str, max_chars: int) -> str:
    """Titre + résumé en Markdown, tronqué, suivi du lien vers la note."""
    title, blocks, current = None, [], None

    for line in md_text.splitlines():
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
        elif line.startswith("## "):
            heading = line[3:].strip()
            if any(k in heading.lower() for k in KEEP_SECTIONS):
                current = [heading]
                blocks.append(current)
            else:
                current = None
        elif current is not None and line.strip() != "---":
            current.append(line)

    header = f"# 📋 {title or f'Veille DPIA — {note_name}'}"
    footer = f"\n\n→ Note complète : {REPO_BASE}/veilles/{note_name}.md"

    body = "\n\n".join("## " + "\n".join(b).strip() for b in blocks).strip()
    if not body:
        return header + footer

    budget = max(max_chars - len(header) - len(footer) - 2, 200)
    if len(body) > budget:
        body = body[:budget].rsplit("\n", 1)[0].rstrip()
    return f"{header}\n\n{body}{footer}"


def to_html(md: str) -> str:
    """Markdown → HTML, pour ce que contiennent les notes : titres, puces, gras, code."""
    out, in_list = [], False
    for line in md.splitlines():
        text = escape(line.strip(), quote=False)
        if not text:
            continue
        text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
        text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
        text = re.sub(r"(https?://[^\s<]*[^\s<.,;:!?)])", r'<a href="\1">\1</a>', text)
        item = re.match(r"[-*] +(.*)", text)
        if in_list and not item:
            out.append("</ul>")
            in_list = False
        if item:
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{item.group(1)}</li>")
        elif text.startswith("#"):
            # Titres décalés de deux niveaux : le # de la note devient <h3>.
            level = min(len(text) - len(text.lstrip("#")) + 2, 6)
            out.append(f"<h{level}>{text.lstrip('# ')}</h{level}>")
        else:
            out.append(f"<p>{text}</p>")
    if in_list:
        out.append("</ul>")
    return "".join(out)


def sent_record(note_name: str, fingerprint: str) -> dict | None:
    """Renvoie l'envoi précédent si la note a déjà été postée à l'identique."""
    path = STORE / "sent" / f"{note_name}.json"
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return record if record.get("fingerprint") == fingerprint else None


async def send(message: str, cfg: dict) -> str:
    """Poste le message et renvoie l'event_id confirmé par le serveur."""
    from nio import AsyncClient, AsyncClientConfig, LoginResponse, RoomSendResponse

    for name in ("nio", "nio.crypto", "peewee"):
        logging.getLogger(name).setLevel(logging.CRITICAL)

    STORE.mkdir(parents=True, exist_ok=True)
    creds_file = STORE / "credentials.json"
    client = AsyncClient(
        cfg["homeserver"],
        cfg["username"],
        config=AsyncClientConfig(encryption_enabled=True, store_sync_tokens=True),
        store_path=str(STORE),
    )
    try:
        # Token réutilisé entre les runs : évite une session Tchap par exécution.
        if creds_file.exists():
            client.restore_login(**json.loads(creds_file.read_text(encoding="utf-8")))
        else:
            resp = await client.login(cfg["password"], device_name="veille-dpia")
            if not isinstance(resp, LoginResponse):
                raise RuntimeError(f"login refusé : {resp}")
            creds_file.write_text(
                json.dumps(
                    {
                        "user_id": client.user_id,
                        "device_id": client.device_id,
                        "access_token": client.access_token,
                    },
                    indent=2,
                ),
                encoding="utf-8",
            )

        if client.store is None:
            client.load_store()
        await client.sync(timeout=30000, sync_filter=SYNC_FILTER)
        if client.should_upload_keys:
            await client.keys_upload()

        resp = await client.room_send(
            cfg["room_id"],
            "m.room.message",
            {
                "msgtype": "m.text",
                "body": message,
                "format": "org.matrix.custom.html",
                "formatted_body": to_html(message),
            },
            ignore_unverified_devices=True,
        )
        if not isinstance(resp, RoomSendResponse):
            raise RuntimeError(f"envoi non confirmé : {resp}")
        return resp.event_id
    finally:
        await client.close()


def fail(reason: str) -> int:
    print(f"[tchap] {reason}", file=sys.stderr)
    print("TCHAP_RESULT=failed")
    return 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--note", required=True, help="note .md du jour")
    ap.add_argument("--max-chars", type=int, default=MAX_CHARS)
    ap.add_argument("--dry-run", action="store_true", help="affiche sans envoyer")
    ap.add_argument("--force", action="store_true", help="renvoie (usage manuel)")
    args = ap.parse_args()

    note = Path(args.note)
    if not note.exists():
        return fail(f"note introuvable : {note}")

    message = build_message(
        note.read_text(encoding="utf-8"), note.stem, args.max_chars
    )

    if args.dry_run:
        print(message)
        print(f"TCHAP_RESULT=dry_run chars={len(message)}")
        return 0

    missing = [v for v in ENV_VARS if not os.environ.get(v)]
    if missing:
        return fail(f"variables manquantes : {', '.join(missing)}")
    cfg = {key.split("_", 1)[1].lower(): os.environ[key] for key in ENV_VARS}

    fingerprint = hashlib.sha256(
        f"{cfg['room_id']}|{note.stem}|{message}".encode("utf-8")
    ).hexdigest()[:16]

    if not args.force:
        previous = sent_record(note.stem, fingerprint)
        if previous:
            event_id = previous.get("event_id")
            print(f"[tchap] déjà envoyé (event_id={event_id}) — aucun envoi.")
            print(f"TCHAP_RESULT=already_sent event_id={event_id} chars={len(message)}")
            return 0

    try:
        event_id = asyncio.run(send(message, cfg))
    except Exception as exc:  # noqa: BLE001 — on veut un code de sortie fiable
        return fail(f"échec : {type(exc).__name__}: {exc}")

    record = STORE / "sent" / f"{note.stem}.json"
    record.parent.mkdir(parents=True, exist_ok=True)
    record.write_text(
        json.dumps(
            {"fingerprint": fingerprint, "event_id": event_id, "chars": len(message)},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"[tchap] envoyé — event_id={event_id} ({len(message)} caractères)")
    print(f"TCHAP_RESULT=sent event_id={event_id} chars={len(message)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
