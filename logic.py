import asyncio
import re

#commands
def pubAccount(cmd):
    cmd_account = re.compile(r"\/account ")
    match = cmd_account.match(cmd)
    if(match != None):
        return True
    else:
        return False




#-------------------------------------------#
#-----------------PUBLI_FUNC----------------#
#-------------------------------------------#


async def sendWelcome(event):
    await event.reply(lbl.startWelcomeMessage)

async def sendHelp(event):
    await event.reply('This is **HELP!**')

async def sendAccount(event):
    cmd = event.message.message
    uid = event.message.from_id
    number = cmd.split("/account ")
    await event.reply('This is **Account!**\nNum Set to ' + number[1])








#-------------------------------------------#
#-----------------ADMIN_FUNC----------------#
#-------------------------------------------#

async def listAllPublishers(event):
    await event.reply("THIS is **ALL PUBLISHERS**")

