import data
from pyrogram import types
from modules.quick_translate import quick_translate
from data import quick_translate_chats

def quick_translate_handler(client: types.User, message:types.Message):
    if message.chat.id in quick_translate_chats:
        quick_translate(client, message, "fr", "uk")