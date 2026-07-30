import os
import asyncio
from datetime import datetime
from zoneinfo import ZoneInfo

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session = os.environ["SESSION_STRING"]

client = TelegramClient(StringSession(session), api_id, api_hash)

async def main():
    await client.start()

    berlin = ZoneInfo("Europe/Berlin")
    now = datetime.now(berlin)

    bio = f"🕒 {now.strftime('%H:%M')}"

    await client(UpdateProfileRequest(about=bio))

    await client.disconnect()

asyncio.run(main())