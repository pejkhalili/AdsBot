# import vars as a
# import asyncio
# from telethon import TelegramClient, sync
# from telethon.tl import functions, types
# from telethon.errors import ChannelInvalidError,ChannelPrivateError, MessageIdsEmptyError




# client = TelegramClient(a.session,a.api_id,a.api_hash)

# print("Running...")
# client.start()

# import MySQLdb
# c = MySQLdb.connect(
#     host="127.0.0.1",
#     user="root",
#     password="",
#     db = "ana_api")
#
# users = c.cursor(MySQLdb.cursors.DictCursor)
#
# users.execute("""SELECT * FROM USERS""")
# res = users.fetchall()
# for re in res:
#     print(re['email'])


import sys
cid = sys.argv[1]
print(cid)