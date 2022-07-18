
import pyrogram
from pyrogram.enums.parse_mode import ParseMode
from mtranslate import translate as translateFunc
from pyrogram.types import Message
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random

def translate(client, message: Message, from_lang, to_lang, prefix):
    message_text = message.text

    orig_text = ""
    if message.reply_to_message == None:
        try:
            orig_text = message_text.split(prefix, maxsplit=1)[1]
        except:
            print("error")
            return
    else:
        if message.reply_to_message.text == None:
            return
        orig_text = message.reply_to_message.text
    translate = translateFunc(orig_text, to_lang, from_lang)
    trans_text = translate

    text = "Translate:\n\n{0}".format(trans_text)
    
    reply_message_id = message.id
    photos = [
        'http://imgur.com/a/JbMNmeB',
        'http://imgur.com/a/yX3EErI',
        'http://imgur.com/a/2XHLmDz',
        'http://imgur.com/a/UiGpA7x',
        'http://imgur.com/a/QApS3jW'
    ]

    rand = random.randint(0, 4)

    if message.reply_to_message != None:

        reply_message_id = message.reply_to_message.id
        client.send_photo(message.chat.id, photos[rand], text, ParseMode.MARKDOWN, reply_to_message_id=reply_message_id)
        return

    client.send_photo(message.chat.id, photos[rand], text, ParseMode.MARKDOWN, reply_to_message_id=reply_message_id)

def short_translate(client, message: Message, from_lang, to_lang, prefix):
    message_text = message.text

    orig_text = ""
    if message.reply_to_message == None:
        try:
            orig_text = message_text.split(prefix, maxsplit=1)[1]
        except:
            print("error")
            return
    else:
        if message.reply_to_message.text == None:
            return
        orig_text = message.reply_to_message.text
    translate = translateFunc(orig_text, to_lang, from_lang)
    trans_text = translate

    text = f"{message.from_user.first_name}:\n\n{trans_text}"
    
    reply_message_id = message.id

    rand = random.randint(0, 4)

    if message.reply_to_message != None:

        reply_message_id = message.reply_to_message.id
        client.send_message(message.chat.id, text, ParseMode.MARKDOWN, reply_to_message_id=reply_message_id)
        return

    client.send_message(message.chat.id, text, ParseMode.MARKDOWN, reply_to_message_id=reply_message_id)