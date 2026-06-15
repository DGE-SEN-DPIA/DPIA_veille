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
import simplematrixbotlib as botlib
from nio.rooms import MatrixRoom

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

    # Sync minimal (incrémental) pour initialiser l'état olm/device du compte.
    await client.sync(timeout=30000, full_state=False)
    creds.session_write_file()

    # Un sync incrémental ne renvoie pas forcément l'état du salon visé s'il
    # n'y a pas eu d'activité récente. On l'enregistre manuellement comme
    # salon chiffré : room_send se chargera de récupérer membres et clés.
    if room_id not in client.rooms:
        client.rooms[room_id] = MatrixRoom(room_id, client.user_id, encrypted=True)

    await bot.api.send_text_message(room_id, message)
    await client.close()

if __name__ == "__main__":
    message = sys.argv[1] if len(sys.argv) > 1 else "(message vide)"
    asyncio.run(send_once(message))
