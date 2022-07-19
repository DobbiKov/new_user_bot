import speech_recognition as sr
from pydub import AudioSegment
from mtranslate import translate as translateFunc
import os
# import SpeechRecognition as sr

r = sr.Recognizer()

def translate_voice_bilingual(file_name):
    with sr.AudioFile(file_name) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text_fr = ""
        text_ua = ""

        try:
            text_fr = r.recognize_google(audio_data, language="fr-FR", show_all=True)
            text_ua = r.recognize_google(audio_data, language="uk-UA", show_all=True)
            french_text = french_confidence = ukrainian_text = ukrainian_confidence = None
            try:
                french_text = text_fr["alternative"][0]["transcript"]
                french_confidence = text_fr["alternative"][0]["confidence"]
            except: 
                french_text = ""
                french_confidence = 0

            try:
                ukrainian_text = text_ua["alternative"][0]["transcript"]
                ukrainian_confidence = text_ua["alternative"][0]["confidence"]
            except:
                ukrainian_text = ""
                ukrainian_confidence = 0

            
        except: 
            pass

        return text_fr, text_ua
def translate_voice(file_name):
    with sr.AudioFile(file_name) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text_fr = ""
        text_ua = ""

        try:
            text_fr = r.recognize_google(audio_data, language="fr-FR", show_all=True)
            text_ua = r.recognize_google(audio_data, language="uk-UA", show_all=True)
            french_text = french_confidence = ukrainian_text = ukrainian_confidence = None
            try:
                french_text = text_fr["alternative"][0]["transcript"]
                french_confidence = text_fr["alternative"][0]["confidence"]
            except: 
                french_text = ""
                french_confidence = 0

            try:
                ukrainian_text = text_ua["alternative"][0]["transcript"]
                ukrainian_confidence = text_ua["alternative"][0]["confidence"]
            except:
                ukrainian_text = ""
                ukrainian_confidence = 0

            if french_confidence == ukrainian_confidence and french_confidence == 0:
                return "", None
            if french_confidence >= ukrainian_confidence:
                return french_text, "fr"
            return ukrainian_text, "uk"
        except: 
            pass

        return 

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

def translate_voice_text(text, lang):
    if lang == "uk":
        translated_text = translateFunc(text, "fr", "uk")
        return translated_text
    translated_text = translateFunc(text, "uk", "fr")
    return translated_text


def translate_voice_texts(text_fr, text_ua):
    translated_text_ua = translateFunc(text_fr, "uk", "fr")
    translated_text_fr = translateFunc(text_ua, "fr", "uk")

    return translated_text_fr, translated_text_ua