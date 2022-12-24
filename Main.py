import pyttsx3
import speech_recognition as sr
import os
from Feature import *
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def Speak(audio):
    print(f"Karen:{audio}")
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
def takecommand_hindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi')
        print(f'User said: {query}\n')
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
def Taskexe():
    while True:
        query=takecommand().lower()
        if 'Youtube search' in query:
            youtubesearch(query)
        elif 'search' in query:
            GoogleSearch(query)
        elif 'send mail to myself' in query:
            Speak("To whom")
            to=takecommand()
            Speak("What should I Say")
            content=takecommand()
            sendEmail(to,content)
        elif 'alarm' in query:
            Alarm(query)
        elif 'download image' in query:
            Image(query)
        elif 'exit' in query:
            exit()
Taskexe()