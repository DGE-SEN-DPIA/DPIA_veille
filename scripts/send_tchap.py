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
import simplematrixbotlib as botlib

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

    sent = False

    @bot.listener.on_startup
    async def on_ready(room_id_arg):
        nonlocal sent
        if not sent:
            sent = True
            await bot.api.send_text_message(room_id, message)
            await bot.api.async_client.close()

    await bot.main()

if __name__ == "__main__":
    message = sys.argv[1] if len(sys.argv) > 1 else "(message vide)"
    asyncio.run(send_once(message))
