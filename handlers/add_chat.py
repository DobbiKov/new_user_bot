from dataclasses import dataclass
from pyrogram import Client, filters
from pyrogram import types
from modules.translate_voice import delete_files, translate_voice, convert_ogg_wav, translate_voice_texts, translate_voice_text, text_to_speech
from modules.database import create_chats_for_translating, select_chat_by_chatid
from data import database_connection
import datetime

async def add_chat_handler(client: Client, message: types.Message):
    chats = select_chat_by_chatid(database_connection, message.chat.id)
    if chats and chats[0][3] == message.chat.id:
        return await client.send_message(message.chat.id, f"The chat {message.chat.id} is already in your translation list!")
    full_name = message.chat.first_name
    if message.chat.last_name:
        full_name += (" " + message.chat.last_name)
    chat = (full_name, str(datetime.datetime.now()), message.chat.id)
    create_chats_for_translating(database_connection, chat)
    await client.send_message(message.chat.id, f"Chat id {message.chat.id} was added to the translation list")