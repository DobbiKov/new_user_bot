from pyrogram import Client, filters
from pyrogram import types
from pyrogram.handlers import message_handler

from pyrogram import filters

# from config import api_id, api_hash

from handlers.handle_voice import get_voice
from handlers.help_commands import helpall
from handlers.translates import translateen, translateru, translatefr, translateua
from handlers.not_at_home import im_not_at_home,change_im_here
from handlers.shortcuts import short_tanks
from handlers.beautiful_type import beautiful_type
from handlers.google_search import google_search
from handlers.mafia_call import mafia
from handlers.get_chat_id import get_chat_id
from handlers.without_handlers import without_handlers

# app = Client("my_account", api_id=api_id, api_hash=api_hash)
app = Client("my_account")

app.add_handler(message_handler.MessageHandler(get_voice, filters=filters.voice))
app.add_handler(message_handler.MessageHandler(helpall, filters=filters.command("help", prefixes="#")))

app.add_handler(message_handler.MessageHandler(translateen, filters=filters.command("en", prefixes="#")))
app.add_handler(message_handler.MessageHandler(translateru, filters=filters.command("ru", prefixes="#")))
app.add_handler(message_handler.MessageHandler(translatefr, filters=filters.command("fr", prefixes="#")))
app.add_handler(message_handler.MessageHandler(translateua, filters=filters.command("ua", prefixes="#")))

app.add_handler(message_handler.MessageHandler(get_chat_id, filters=filters.command("get_chat_id", prefixes="#") & filters.me))
app.add_handler(message_handler.MessageHandler(mafia, filters=filters.command("mafia", prefixes="#") & filters.me))
app.add_handler(message_handler.MessageHandler(google_search, filters=filters.command("23", prefixes="#")))
app.add_handler(message_handler.MessageHandler(beautiful_type, filters=filters.command("type", prefixes=".") & filters.me))
app.add_handler(message_handler.MessageHandler(short_tanks, filters=filters.command("спс", prefixes=".") & filters.me))
app.add_handler(message_handler.MessageHandler(change_im_here, filters=filters.command("тут", prefixes=".") & filters.me))
app.add_handler(message_handler.MessageHandler(without_handlers))

app.run()

