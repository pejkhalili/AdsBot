import vars as a
import labels as lbl
import logic as logi
import asyncio
from telethon import TelegramClient, sync
from telethon import events

client = TelegramClient(a.session,a.api_id,a.api_hash)
 



@client.on(events.NewMessage(incoming=True))
async def handler(event):
    cmd = event.message.message
    uid = event.message.from_id
    print(uid)
    print(cmd)
    print(logi.pubAccount(cmd))
    
    
    #check user to be admin
    for admin in a.adminUsers:
        if admin == uid: a.is_admin=True

    ## Admins Commands
    if a.is_admin :          
        if(cmd == "listPubs"):
            await logi.listAllPublishers(event)

    ## Publisher Commands
    else:
        if(cmd == "/start"):
            await logi.sendWelcome(event)
            
        elif(logi.pubAccount(cmd)):
            print("in Account")
            await logi.sendAccount(event)

        else:
            await logi.sendHelp(event)
    


async def main():
    print("Running...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

#//////////////////////////////
# auto reply

# from telethon import events

# @client.on(events.NewMessage(incoming=True,pattern='(?i)hi'))
# async def handler(event):
#     await event.reply('hello')
# client.run_until_disconnected()

#///////////////////////////////
# self infos
# me = client.get_me()

# from telethon import utils
# Retrieving messages from a chat

# for message in client.iter_messages('me',limit = 10):
#     print(utils.get_display_name(message.sender), message.message)

# List All Dialogs in chat

# for dialog in client.get_dialogs(limit=1000):
#     print(dialog.name, dialog.draft.text)

# client.download_profile_photo('namaZhe')
