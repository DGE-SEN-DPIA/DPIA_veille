#!/usr/bin/env python3
"""
Envoie un message dans un salon Tchap chiffré via l'API Matrix.
Usage : python scripts/send_tchap.py "Message à envoyer"
Credentials lus depuis les variables d'environnement :
  TCHAP_HOMESERVER, TCHAP_USERNAME, TCHAP_PASSWORD, TCHAP_ROOM_ID
Le dossier crypto_store/ doit exister dans le repo (persistance des clés E2E).
"""
import asyncio
import os
import sys
import cryptography
import aiohttp
import simplematrixbotlib as botlib
from nio.rooms import MatrixRoom

# aiohttp ne lit pas HTTPS_PROXY (majuscules) automatiquement.
# On force trust_env=True sur tous les ClientSession créés (y.c. ceux de matrix-nio).
_orig_cs_init = aiohttp.ClientSession.__init__
def _patched_cs_init(self, *args, **kwargs):
    kwargs.setdefault("trust_env", True)
    _orig_cs_init(self, *args, **kwargs)
aiohttp.ClientSession.__init__ = _patched_cs_init

# Expose aussi les variantes minuscules au cas où
if "HTTPS_PROXY" in os.environ:
    os.environ.setdefault("https_proxy", os.environ["HTTPS_PROXY"])
if "HTTP_PROXY" in os.environ:
    os.environ.setdefault("http_proxy", os.environ["HTTP_PROXY"])

async def send_once(message: str):
    homeserver = os.environ["TCHAP_HOMESERVER"]
    username   = os.environ["TCHAP_USERNAME"]
    password   = os.environ["TCHAP_PASSWORD"]
    room_id    = os.environ["TCHAP_ROOM_ID"]

    # Chemin relatif au repo — doit être persistant entre les runs
    store_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "crypto_store"
    )
    os.makedirs(store_path, exist_ok=True)

    # Configuration avec chiffrement activé
    config = botlib.Config()
    config.encryption_enabled        = True
    config.ignore_unverified_devices = True   # accepte tous les appareils du salon
    config.store_path                = store_path

    creds = botlib.Creds(homeserver, username, password)
    bot   = botlib.Bot(creds, config)

    # On évite bot.main() : sa boucle sync_forever() ne se termine jamais.
    # On reproduit juste le strict nécessaire pour envoyer un message chiffré.
    try:
        creds.session_read_file()
    except cryptography.fernet.InvalidToken:
        os.remove(creds._session_stored_file)
        creds.session_read_file()

    await bot.api.login()
    client = bot.api.async_client

    # Force l'utilisation du proxy : injecte un ClientSession avec trust_env=True
    # avant le premier appel réseau (client_session peut être None si login était en cache).
    if hasattr(client, "client_session") and client.client_session:
        await client.client_session.close()
    client.client_session = aiohttp.ClientSession(trust_env=True)

    # Sync minimal pour initialiser l'état olm/device du compte.
    # timeout=0 : le serveur répond immédiatement sans long-poll (évite le timeout proxy).
    await client.sync(timeout=0, full_state=False)
    creds.session_write_file()

    # Enregistre le salon si absent du sync (pas d'activité récente).
    if room_id not in client.rooms:
        client.rooms[room_id] = MatrixRoom(room_id, client.user_id, encrypted=True)

    # Récupère membres ET clés des appareils, requis pour partager la clé de
    # session Megolm à tous les destinataires (sinon message non déchiffrable).
    # /!\ joined_members() met members_synced=True, ce qui fait sauter à room_send()
    # son bloc interne joined_members()+keys_query() : on doit donc appeler
    # keys_query() nous-mêmes ici, sinon le device_store reste vide et la clé
    # de session n'est partagée avec personne.
    await client.joined_members(room_id)
    if client.should_query_keys:
        await client.keys_query()

    await bot.api.send_text_message(room_id, message)
    await client.close()

if __name__ == "__main__":
    message = sys.argv[1] if len(sys.argv) > 1 else "(message vide)"
    asyncio.run(send_once(message))
