from pyrogram import Client, filters
from pyrogram import types
from modules.translate_voice import delete_files, translate_voice, convert_ogg_wav, translate_voice_texts, translate_voice_text, text_to_speech

async def get_voice(client: Client, message: types.Message):
    if message.chat.id < 0 and message.chat.id != -1001711218638 and message.chat.id != -640017880:
        return False
    new_mess = await client.send_message(message.chat.id, "Please, wait...")
    # await client.send_message(message.chat.id, "о, повідомлення голосове")
    print(message.voice.file_id)
    file = await client.download_media(message.voice.file_id)

    file_name = file #/Users/dsadas/
    # # file_bytes = bytes(file.getbuffer())
    file_path = convert_ogg_wav(file_name)
    text, lang = await translate_voice(file_path)

    if lang == None:
        try:
            await client.edit_message_text(new_mess.chat.id, new_mess.id, "I haven't understood your message. Try again please")
        except:
            pass
        delete_files(file_path)
        return

    translated_text, translated_lang = translate_voice_text(text, lang)

    text_message = f"\
{message.from_user.first_name}:\n\n\
{text}\n\n\
Translation:\n\
{translated_text}"

    try:
        await client.edit_message_text(new_mess.chat.id, new_mess.id, text_message)
    except:
        pass
    new_voice = text_to_speech(translated_text, translated_lang, file_name)
    await client.send_voice(message.chat.id, new_voice)
    delete_files(file_path)


# async def get_voice(client, message: types.Message):
#     if message.chat.id < 0 and message.chat.id != -1001711218638:
#         return False
#     # await client.send_message(message.chat.id, "о, повідомлення голосове")
#     print(message.voice.file_id)
#     file = await client.download_media(message.voice.file_id)

#     file_name = file #/Users/dsadas/
#     # # file_bytes = bytes(file.getbuffer())
#     file_path = convert_ogg_wav(file_name)
#     text_fr, text_ua = translate_voice(file_path)

#     translated_text_fr, translated_text_ua = translate_voice_texts(text_fr, text_ua)

#     text_message = f"\
# {message.from_user.first_name}:\n\n\
# {text_fr}\n\
# {text_ua}\n\n\
# Translation:\n\
# {translated_text_fr}\n\
# {translated_text_ua}"
#     await client.send_message(message.chat.id, text_message)
#     delete_files(file_path)