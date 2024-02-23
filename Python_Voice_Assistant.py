import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import psutil
import pyautogui
import time

# Set Voice properties using pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)

# Voice change function to Male or Female and vice-versa
def voice_change(v):
    x = int(v)
    engine.setProperty('voice',voices[x].id)
    speak("done sir")

# Speak Function using audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Take command Function using speech_recognition
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening....")
        audio = r.listen(source)
        print("Recognizing.....")
        try:
            query = r.recognize_google(audio)
            print("User said: "+query+"\n")
        except Exception as e:
            print("Error: "+str(e))
            return "None"
        return query
    
# It is a common function which is used to open anything in your PC using pyautogui
def open():
    pyautogui.press("win")
    time.sleep(.5)
    pyautogui.write(query)
    time.sleep(.5)
    pyautogui.press("enter")

def close():
    pyautogui.keyDown("alt")
    pyautogui.hotkey("f4")
    pyautogui.keyUp("alt")

def write():
    pyautogui.write(query)

def save():
    pyautogui.keyDown("ctrl")
    pyautogui.press("s")
    pyautogui.keyUp("ctrl")
    time.sleep(2)
    pyautogui.press("enter")

# Main Program
if __name__ == '__main__':
    speak("Slash Mark Assistant Activated")
    speak("How can i help you")
    while True:
        # take voice command
        query = take_command().lower()
        # search on wikipedia
        if('wikipedia' in query):
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia",'')
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(results)
        # About voice assistant
        elif('are you' in query,'who are you' in query):
            speak("I am Slash Mark Assistant developed by Harshvardhan")
        # for open youtube
        elif 'open youtube' in query:
            speak("ok sir opening youtube")
            wb.open_new_tab("www.youtube.com")
        # for open google
        elif 'open google' in query:
            speak("ok sir opening google")
            wb.open_new_tab("www.google.com")
        # for open github
        elif 'open github' in query:
            speak("ok sir opening github")
            wb.open_new_tab("www.github.com")
        # for open stackoverflow
        elif 'open stackoverflow' in query:
            speak("ok sir opening Stack Overflow")            
            wb.open_new_tab("https://stackoverflow.com/")
        # for open spotify
        elif 'open spotify' in query:
            speak("ok sir opening spotify")
            wb.open_new_tab("https://open.spotify.com/")
        # for open whatsapp
        elif 'open whatsapp' in query:
            speak("ok sir opening whatsapp")
            wb.open_new_tab("https://web.whatsapp.com/")
        # for playing music
        elif 'play music' in query:
            speak("ok sir playing music")
            wb.open_new_tab("https://open.spotify.com/")
        # for open local disk d
        elif 'local disk d' in query:
            speak("ok sir opening local disk d")
            wb.open("D://")
        # for open local disk c
        elif 'local disk c' in query:
            speak("ok sir opening local disk c")
            wb.open("C://")
        # for open local disk e
        elif 'loacl disk e' in query:
            speak("ok sir opening local disk e")
            wb.open("E://")
        # for change voice male to female and vice varsa
        elif("male" in query or "female" in query):
            if("female" in query):
                voice_change(1)
            elif("male" in query):
                voice_change(0)
        # for open any software which is already install in your PC
        elif("open" in query):
            query = query.replace("open","")
            open()
        # for close any open software
        elif("close" in query):
            close()
        # for write anything by your voice command
        elif("write" in query):
            query = query.replace("write","")
            write()
        # for press enter key
        elif("enter" in query):
            pyautogui.press("enter")
        # for save file
        elif("protect" in query,"save" in query):
            save()
        # close terminal
        elif('sleep' in query):
            exit(0)
