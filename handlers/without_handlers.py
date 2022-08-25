import data
from pyrogram import types
from handlers.not_at_home import im_not_at_home
from handlers.quick_translate_handler import quick_translate_handler

def without_handlers(client: types.User, message:types.Message):
    quick_translate_handler(client, message)
    im_not_at_home(client, message)