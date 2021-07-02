import random
from gtts import gTTS
from playsound import playsound
import os
import time
import speech_recognition as sr
import webbrowser
from time import ctime
import datetime

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speaky(ask)

        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            speaky('Sorry,I did not get that')
        except sr.RequestError:
            speaky('Sorry, the service is down')
        return voice_data


def speaky(string):
    tts = gTTS(text=string, lang='en')
    r = random.randint(1, 9000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(string)
    os.remove(audio_file)


hour = int(datetime.datetime.now().hour)


def respond(voice_data):
    if 'thank you' in voice_data:
        speaky('any time sir ')
    if 'search' in voice_data:
        search = record_audio('what do you want search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speaky('Here is what I found for ' + search)

    if 'find location' in voice_data:
        location = record_audio('to where ')
        url = 'https://google.com/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speaky('Here is the location of ' + location)
    if "good bye" in voice_data or "ok bye" in voice_data or "stop" in voice_data or "exit" in voice_data:
        speaky('your personal assistant snoopy  is shutting down,Good bye sir')
        exit()

    if 'time' in voice_data:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speaky(f"the time is {time}")
        
    elif 'who are you' in voice_data or 'what can you do' in voice_data:
        speaky('I am snoopy version 1 point O your personal assistant. I am programmed to minor tasks like'
              'opening youtube,google chrome, gmail ,predict time,take a photo,search wikipedia,predict weather'
              'In different cities,!')

    elif "who made you" in voice_data or "who created you" in voice_data or "who discovered you" in voice_data:
        speaky("I was built by speaky team ")



name = 'niveen'
time.sleep(1)
if hour >= 0 and hour <= 12:
    speaky("Good Morning Name!" + name)
elif hour >= 12 and hour <= 18:
    speaky("Good Afternoon " + name)
else:
    speaky("Good Evening Name!" + name)
speaky("Hey, im snoopy! and im here to serve you ")

while 1:
    voice_data = record_audio()
    respond(voice_data)

# def Name(string):
#     tts = gTTS(text=string, lang='en')
#     audio_file = 'name.mp3'
#     tts.save(audio_file)
#     playsound(audio_file)
#     os.remove(audio_file)
#
#
# def name():
#     with sr.AudioFile(name.file) as source:
#         audio_data = r.record(source)
#         text = sr.recognize_google(audio_data)
#         print(text)