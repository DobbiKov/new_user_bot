from pyrogram import Client, filters
from pyrogram import types
from modules.translate_voice import delete_files, translate_voice, convert_ogg_wav

async def get_voice(client, message: types.Message):
    # await client.send_message(message.chat.id, "о, повідомлення голосове")
    print(message.voice.file_id)
    file = await client.download_media(message.voice.file_id)

    file_name = file #/Users/dsadas/
    # # file_bytes = bytes(file.getbuffer())
    file_path = convert_ogg_wav(file_name)
    text_fr, text_ua = translate_voice(file_path)
    await client.send_message(message.chat.id, f"{message.from_user.first_name}:\n\n{text_fr}\n{text_ua}")
    delete_files(file_path)