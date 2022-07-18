from modules.translate import translate, short_translate

def translateen(client, message):
    translate(client, message, "ru", "en", "#en ")

def translateru(client, message):
    translate(client, message, "en", "ru", "#ru ")

def translatefr(client, message):
    short_translate(client, message, "uk", "fr", "#fr ")

def translateua(client, message):
    short_translate(client, message, "fr", "uk", "#ua ")