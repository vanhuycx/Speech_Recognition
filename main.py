import speech_recognition as sr 
import time 
from time import ctime
import os
from gtts import gTTS
import pyglet
import subprocess
def speak(audio_string):
    print(audio_string)
    tts = gTTS(text=audio_string,lang='en')
    tts.save('speechs.mp3')

    wmp = 'C:\Program Files (x86)\Windows Media Player\wmplayer.exe'
    media_file = os.path.abspath(os.path.realpath("C:\\Users\\baoma\Downloads\\Machine Learning\\Project\\Speech_Recognition\\speechs.mp3"))
    p = subprocess.call([wmp,media_file])

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something!')
        audio = r.listen(source)
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:
        print("Couldn't understand audio")
    except sr.RequestError as e:
        print(f"Couldn't request result {e}")
    return data

def stan(data):
    if 'how are you' in data:
        speak('I am fine')

time.sleep(2)

speak('Hi Van, what can I do for you?')
while 1:
    data = recordAudio()
    stan(data)