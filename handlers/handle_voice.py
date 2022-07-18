from pyrogram import Client, filters
from pyrogram import types
from modules.translate_voice import delete_files, translate_voice, convert_ogg_wav, translate_voice_texts

async def get_voice(client, message: types.Message):
    if message.chat.id < 0 and message.chat.id != -1001711218638:
        return False
    # await client.send_message(message.chat.id, "о, повідомлення голосове")
    print(message.voice.file_id)
    file = await client.download_media(message.voice.file_id)

    file_name = file #/Users/dsadas/
    # # file_bytes = bytes(file.getbuffer())
    file_path = convert_ogg_wav(file_name)
    text_fr, text_ua = translate_voice(file_path)

    translated_text_fr, translated_text_ua = translate_voice_texts(text_fr, text_ua)

    text_message = f"\
{message.from_user.first_name}:\n\n\
{text_fr}\n\
{text_ua}\n\n\
Translation:\n\
{translated_text_fr}\n\
{translated_text_ua}"
    await client.send_message(message.chat.id, text_message)
    delete_files(file_path)