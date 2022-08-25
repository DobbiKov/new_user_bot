import speech_recognition as sr
from pydub import AudioSegment
from mtranslate import translate as translateFunc
import os
from datetime import datetime
from gtts import gTTS
import threading
# import SpeechRecognition as sr

r = sr.Recognizer()

class ThreadRecognize (threading.Thread):
    def __init__(self, audio, language):    # event = objet Event
        threading.Thread.__init__(self)  # = donnée supplémentaire
        self.audio = audio
        self.event = threading.Event()                 # on garde un accès à l'objet Event
        self.event.clear()
        self.language = language
 
    def run(self):
        self.result=r.recognize_google(self.audio, language=self.language, show_all=True)
        self.event.set()
 
    def wait(self):
        self.event.wait()

async def translate_voice(file_name):
    with sr.AudioFile(file_name) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text_fr = ""
        text_ua = ""

        try:
            # text_fr, text_ua = recognize_func(audio_data)
            threads = []
            threads.append(ThreadRecognize(audio_data, language="fr-FR"))
            threads.append(ThreadRecognize(audio_data, language="uk-UA"))
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join() 
            text_fr = threads[0].result
            text_ua = threads[1].result
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

        return "", None

async def recognize_func(audio_data):
    text_fr = r.recognize_google(audio_data, language="fr-FR", show_all=True)
    text_ua = r.recognize_google(audio_data, language="uk-UA", show_all=True)
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
    voice_path = file_name.replace(".wav", "_voice.wav")
    delete_file(export_path)
    delete_file(import_path)
    delete_file(voice_path)

def delete_file(path):
    try:
        os.remove(path)
    except:
        pass

def translate_voice_text(text, lang):
    if lang == "uk":
        translated_text = translateFunc(text, "fr", "uk")
        return translated_text, "fr"
    translated_text = translateFunc(text, "uk", "fr")
    return translated_text, "uk"


def translate_voice_texts(text_fr, text_ua):
    translated_text_ua = translateFunc(text_fr, "uk", "fr")
    translated_text_fr = translateFunc(text_ua, "fr", "uk")

    return translated_text_fr, translated_text_ua

def text_to_speech(text, lang, file_path: str):
    new_path = file_path.replace(".ogg", "_voice.wav")
    myobj = gTTS(text=text, lang=lang, slow=False)
    myobj.save(new_path)
    return new_path