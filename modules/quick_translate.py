from pyrogram.enums.parse_mode import ParseMode
from mtranslate import translate as translateFunc
from pyrogram.types import Message

from time import sleep
import random

def quick_translate(client, message: Message, lang_1, lang_2):
    #lang_1 = fr | lang_2 = uk
    message_text = message.text
    translate_1 = translateFunc(message_text, lang_2, lang_1)
    translate_2 = translateFunc(message_text, lang_1, lang_2)

    trans_text = ""
    if translate_1 != message_text:
        trans_text = translate_1
    else:
        trans_text = translate_2

    # text = f"{message.from_user.first_name}:\n\n{trans_text}"
    text = f"{message.from_user.first_name}:\n\n{translate_1}\n\n{translate_2}"
    
    reply_message_id = message.id

    if message.reply_to_message != None:

        reply_message_id = message.reply_to_message.id
        client.send_message(message.chat.id, text, ParseMode.MARKDOWN, reply_to_message_id=reply_message_id)
        return

    client.send_message(message.chat.id, text, ParseMode.MARKDOWN, reply_to_message_id=reply_message_id)