from pyrogram import Client, filters
from pyrogram import types
from modules.translate_voice import delete_files, translate_voice, convert_ogg_wav, translate_voice_texts, translate_voice_text, text_to_speech

async def get_chat_id(client: Client, message: types.Message):
    await client.send_message(message.chat.id, f"Chat id: {message.chat.id}")