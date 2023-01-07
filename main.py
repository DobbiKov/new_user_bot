from pyrogram import Client, filters
from pyrogram import types
from pyrogram.handlers import message_handler

from pyrogram import filters

import data
from data import sqlite_database_file

from modules.database import create_connection, create_chats_for_translating_table

# from config import api_id, api_hash

from handlers.handle_voice import get_voice
from handlers.help_commands import helpall
from handlers.translates import translateen, translateru, translatefr, translateua
from handlers.not_at_home import im_not_at_home,change_im_here
from handlers.shortcuts import short_tanks
from handlers.beautiful_type import beautiful_type
from handlers.google_search import google_search
from handlers.mafia_call import mafia
from handlers.chatgpt_handler import chatgpt_handler
from handlers.get_chat_id import get_chat_id
from handlers.without_handlers import without_handlers
from handlers.add_chat import add_chat_handler
from handlers.my_trans_chats import my_trans_chats_handler

# app = Client("my_account", api_id=api_id, api_hash=api_hash)

def main():
    app = Client("my_account")

    conn = create_connection(sqlite_database_file)
    data.database_connection = conn
    create_chats_for_translating_table(conn)

    app.add_handler(message_handler.MessageHandler(get_voice, filters=filters.voice))
    app.add_handler(message_handler.MessageHandler(helpall, filters=filters.command("help", prefixes="#")))

    app.add_handler(message_handler.MessageHandler(translateen, filters=filters.command("en", prefixes="#")))
    app.add_handler(message_handler.MessageHandler(translateru, filters=filters.command("ru", prefixes="#")))
    app.add_handler(message_handler.MessageHandler(translatefr, filters=filters.command("fr", prefixes="#")))
    app.add_handler(message_handler.MessageHandler(translateua, filters=filters.command("ua", prefixes="#")))

    app.add_handler(message_handler.MessageHandler(get_chat_id, filters=filters.command("get_chat_id", prefixes="#") & filters.me))
    app.add_handler(message_handler.MessageHandler(mafia, filters=filters.command("mafia", prefixes="#") & filters.me))
    app.add_handler(message_handler.MessageHandler(chatgpt_handler, filters=filters.command("chatgpt", prefixes="#") & filters.me))
    app.add_handler(message_handler.MessageHandler(google_search, filters=filters.command("23", prefixes="#")))
    app.add_handler(message_handler.MessageHandler(beautiful_type, filters=filters.command("type", prefixes=".") & filters.me))
    app.add_handler(message_handler.MessageHandler(short_tanks, filters=filters.command("спс", prefixes=".") & filters.me))
    app.add_handler(message_handler.MessageHandler(change_im_here, filters=filters.command("тут", prefixes=".") & filters.me))

    app.add_handler(message_handler.MessageHandler(add_chat_handler, filters=filters.command("add_chat", prefixes=".") & filters.me))
    app.add_handler(message_handler.MessageHandler(my_trans_chats_handler, filters=filters.command("my_trans_chats", prefixes=".") & filters.me))
    app.add_handler(message_handler.MessageHandler(without_handlers))

    print("The bot was started!")
    my_id = 716720991
    # app.send_message(my_id, "The bot had been started!")
    app.run()

if __name__ == '__main__':
    main()
