import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

print('Initializing Jarvis..')
master = 'Shekhar'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait() 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning {master}. its{hour} oclock")
    elif hour>=12 and hour<=17:
        speak(f"Good afternoon {master}. its{hour} oclock")
    else:
        speak(f"Good evening {master}. its{hour} oclock")

    speak(f"How mmay I help You {master}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except:
        print("Say that again please")        



speak('Initializing Jarvis')
wishMe()
takeCommand()