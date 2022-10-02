import speech_recognition as sr
import datetime
import webbrowser
import subprocess
import pyttsx3
import pywhatkit
import pyautogui

# create instance for python text to speech library
engine = pyttsx3.init()

# get object of engine
voices = engine.getProperty('voices')

# assign male or female voices
engine.setProperty('voice',voices[7].id) # female 1, male 0

# speech recognizer
recognizer = sr.Recognizer()

whtcall ="Hey,What do i call you ?"
engine.say(whtcall)
engine.runAndWait()
name=input("Your name : ")
x= f"Hello {name}, How Can i help you ? You can Ask Anything you wanted to"
engine.say(x)
engine.runAndWait()

def cmd():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source,duration=1)
        print("now ask")
        recordedaudio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
#         print('urmessage:',format(text))
        if 'time' in text:
            time = datetime.datetime.now().strftime('%I:%M %p')
#             print(time)
            engine.say(time)
            engine.runAndWait()
        if 'play' in text:
            a='opening youtube..'
            engine.say(a)
            engine.runAndWait()
            pywhatkit.playonyt(text)
        if 'youtube' in text:
            b='opening youtube'
            engine.say(b)
            engine.runAndWait()
            def error404():
                return webbrowser.open('http://youtube.in')
            error404()
        if "google" in text:
            b="opening google"
            engine.say(b)
            engine.runAndWait()
            def error404():
                webbrowser.open('http://google.in')
            error404()
        if "screenshot" in text:
            b="Screenshot Taken Successfully !"
            engine.say(b)
            engine.runAndWait()
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'screenshot_1.png')
        if ("goodbye" or "bye") in text:
            b=f"bye {name}"
            engine.say(b)
            engine.runAndWait()
            return
    except Exception as ex:
            print(ex)
    
while True:
    cmd()
