import speech_recognition as sr
from pydub import AudioSegment
from mtranslate import translate as translateFunc
import os
# import SpeechRecognition as sr

r = sr.Recognizer()

def translate_voice(file_name):
    with sr.AudioFile(file_name) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text_fr = ""
        text_ua = ""

        try:
            text_fr = r.recognize_google(audio_data, language="fr-FR")
            text_ua = r.recognize_google(audio_data, language="uk-UA")
        except: 
            pass

        return text_fr, text_ua

def convert_ogg_wav(file_path):
    sound = AudioSegment.from_ogg(file_path)
    export_path = file_path.replace(".ogg", ".wav")
    # path_export_name = f"./downloads/{export_name}"
    sound.export(export_path, format="wav")
    return export_path

def delete_files(file_name):
    export_path = file_name
    import_path = file_name.replace(".wav", ".ogg")
    os.remove(export_path)
    os.remove(import_path)

def translate_voice_texts(text_fr, text_ua):
    translated_text_ua = translateFunc(text_fr, "uk", "fr")
    translated_text_fr = translateFunc(text_ua, "fr", "uk")

    return translated_text_fr, translated_text_ua