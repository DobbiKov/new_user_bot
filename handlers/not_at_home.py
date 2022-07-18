import data
from pyrogram import types

def change_im_here(client, message):
    data.im_here = not data.im_here
    here_mess = ""
    if data.im_here == True:
        here_mess = "на месте."
    else:
        here_mess = "не на месте."
    
    message.edit(f"Вы: {here_mess}")

def im_not_at_home(client: types.User, message:types.Message):
    date = "18.10.2021"
    if message.chat.id > 0 and data.im_here == False:
        send_im_not_here(client, message, date)
    elif "@dobbikov" in message.text and data.im_here == False and message.chat.type == "group":
        send_im_not_here(client, message, date)

def send_im_not_here(client, message, date):
    client.send_message(message.chat.id, f"**I'm haven't access to my phone at the moment.** \n\n\
I will be able to answer: **{date}**.\n\n\
See you soon!", parse_mode="markdown")