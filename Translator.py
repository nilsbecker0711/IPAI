#Author: Nils Becker

from googletrans import Translator
import googletrans
from gtts import gTTS
import playsound
import speech_recognition as sr 
import os

def speechToText(origin):
    '''
    This method converts a spoken text into a string
    '''
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start speaking: ")
        audio = recognizer.listen(source)
        text = ""
        lan = origin + "-"+ origin.upper()
        try:
            text = recognizer.recognize_google(audio, language = lan)
        except :
            print("Not Audible")
            return ""
    return text


def translate (input, lang):
    '''
    This method translates a given input to english
    using the google translate library
    '''
    translator = Translator()
    return translator.translate(input, lang).text

def textToSpeech(output, lang):
    '''
    This method converts an input string to a audio file and plays this file
    '''
    tts = gTTS(text=output, lang = lang)
    tempFile = os.path.dirname(os.path.realpath(__file__)) + 'temp.mp3'
    tts.save(tempFile)
    try:
        playsound.playsound(tempFile)
    except:
        textToSpeech(output, lang)


languages = googletrans.LANGUAGES

origin = ""
while origin == "":
    origin = input("Enter the origin language: ").lower()
    if(origin not in languages.values()):
        origin = ""
    else:
        origin = list(languages.keys())[list(languages.values()).index(origin)]

destination =""
while destination == "":
    destination = input("Enter the destionation language: ").lower()
    if(destination not in languages.values()):
        destination = ""
    else:
        destination = list(languages.keys())[list(languages.values()).index(destination)]

input = ""
while input == "": 
    input = speechToText(origin)
translation = translate(input, destination)
print(input, "->", translation)
textToSpeech(translation, destination)
