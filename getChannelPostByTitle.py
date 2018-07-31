import vars as a
import asyncio
from telethon import TelegramClient, sync
from telethon.tl.functions.messages import GetHistoryRequest


client = TelegramClient(a.session,a.api_id,a.api_hash)


channel_username='@namazh' # your channel
searchVal ="چرادلار امروز ۱۲۰۰۰ تومن نشده؟ چه کسی پاسخگوئه؟ چه خبرتونههه؟ هان؟ \n\nYasiN @Namazh"


print("Running...")
client.start()
channel_entity=client.get_entity(channel_username)
posts = client(GetHistoryRequest(
    peer=channel_entity,
    limit=0,
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0,
    hash=0))

msgs = posts.messages
print(posts.count)
i = 0
for msg in msgs:
    if msg.message == searchVal:
        rank = i
        # print (msg)
        print("place:" + str(rank))
        print("View Count:" + str(msg.views))
        print ("Date: " + str(msg.date))
        print("msg_id: " + str(msg.id))
        break
    i = i+1
    print("Searching...")
