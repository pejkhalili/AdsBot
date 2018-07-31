import vars as a
import asyncio
from telethon import TelegramClient, sync
from telethon.tl import functions, types
from telethon.errors import ChannelInvalidError,ChannelPrivateError, MessageIdsEmptyError




client = TelegramClient(a.session,a.api_id,a.api_hash)

print("Running...")
client.start()
