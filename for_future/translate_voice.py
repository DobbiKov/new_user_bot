import speech_recognition as sr
from pydub import AudioSegment
from mtranslate import translate as translateFunc
import os
from .voiceParametres import VoiceParametres
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

        languages = []
        languages.append(VoiceParametres("fr"))
        languages.append(VoiceParametres("uk"))
        languages.append(VoiceParametres("en"))
        languages.append(VoiceParametres("ru"))

        recognitions = []

        try:
            recognitions.append(r.recognize_google(audio_data, language="fr-FR", show_all=True))
            recognitions.append(r.recognize_google(audio_data, language="uk-UA", show_all=True))
            recognitions.append(r.recognize_google(audio_data, language="es-US", show_all=True))
            recognitions.append(r.recognize_google(audio_data, language="ru-RU", show_all=True))
            # text_fr = r.recognize_google(audio_data, language="fr-FR", show_all=True)
            # text_ua = r.recognize_google(audio_data, language="uk-UA", show_all=True)
            # text_en = r.recognize_google(audio_data, language="es-US", show_all=True)
            # text_ru = r.recognize_google(audio_data, language="ru-RU", show_all=True)

            for i in range(4):
                languages[i].text = recognitions[i]["alternative"][0]["transcript"]
                languages[i].confidence = recognitions[i]["alternative"][0]["confidence"]

            # try:
            #     french_text = text_fr["alternative"][0]["transcript"]
            #     french_confidence = text_fr["alternative"][0]["confidence"]
            # except: 
            #     french_text = ""
            #     french_confidence = 0

            # try:
            #     ukrainian_text = text_ua["alternative"][0]["transcript"]
            #     ukrainian_confidence = text_ua["alternative"][0]["confidence"]
            # except:
            #     ukrainian_text = ""
            #     ukrainian_confidence = 0
            ret_text, ret_lang = biggest_confidence(languages)
            return ret_text, ret_lang
            # if french_confidence == ukrainian_confidence and french_confidence == 0:
            #     return "", None
            # if french_confidence >= ukrainian_confidence:
            #     return french_text, "fr"
            # return ukrainian_text, "uk"
        except: 
            pass

        return 
def biggest_confidence(list_langs):
    first_element = list_langs[0]
    is_different = False
    for i in list_langs:
        if i.confidence != first_element.confidence:
            is_different = True
            break
    if is_different == False:
        return "", None
    
    biggest = VoiceParametres("None")
    for i in list_langs:
        if i.confidence > biggest.confidence:
            biggest = i
    return biggest.text, biggest.lang



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
    langs = ["fr", "uk", "en", "ru"]
    langs.remove(lang)
    translated_text = "\n"
    for i in langs:
        temp_text = translateFunc(text, i, lang)
        translated_text += f"{temp_text}\n"

    return translated_text
    # if lang == "uk":
    #     translated_text = translateFunc(text, "fr", "uk")
    #     return translated_text
    # translated_text = translateFunc(text, "uk", "fr")
    # return translated_text


def translate_voice_texts(text_fr, text_ua):
    translated_text_ua = translateFunc(text_fr, "uk", "fr")
    translated_text_fr = translateFunc(text_ua, "fr", "uk")

    return translated_text_fr, translated_text_ua

