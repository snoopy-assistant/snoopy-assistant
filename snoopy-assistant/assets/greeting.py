import random
from gtts import gTTS
from playsound import playsound
import os
import time
import times
import speech_recognition as sr
import webbrowser
from time import ctime
import datetime
from pygame import mixer

r = sr.Recognizer()


class person:
    name = ''

    def setName(self, name):
        self.name = name


class asis:
    name = ''

    def setName(self, name):
        self.name = name


person_obj = person()
asis_obj = asis()
asis_obj.name = 'snoopy'
person_obj.name = ""


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speaky(ask)

        audio = r.listen(source, timeout=5)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            speaky('Sorry,I did not get that repeat it ')
        except sr.RequestError:
            speaky('Sorry, the service is down')
        return voice_data


def speaky(string):
    tts = gTTS(text=string, lang='en', slow=False)
    r = random.randint(1, 9000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(string)
    os.remove(audio_file)


hour = int(datetime.datetime.now().hour)


################################################################################
########################### Name ####################################


def Name(voice_data):
    if "what is your name" in voice_data or "what's your name" in voice_data or "tell me your name" in voice_data:

        if person_obj.name:
            speaky(f"My name is {asis_obj.name}, {person_obj.name}")
        else:
            speaky(f"My name is {asis_obj.name}. what's your name?")

    if "my name is" in voice_data:
        person_name = voice_data.split("is")[-1].strip()
        speaky("okay, i will remember that " + person_name)
        speaky('how your day going?'+person_name)
        person_obj.setName(person_name)


def respond(voice_data):
    if 'hey' in voice_data or 'hi ' in voice_data or 'hello 'in voice_data:
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name,
                     "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name,
                     "hello" + person_obj.name]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speaky(greet)

    if 'good' in voice_data or 'nice' in voice_data or 'perfect' in voice_data:
        speaky('hopefully forever ')
    if 'not' in voice_data or 'mad' in voice_data:
        speaky(' Do not worry , snoopy will make it right ')
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

    if "what is my exact location" in voice_data:
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        speaky("You must be somewhere near here, as per Google maps")   
    if "bye" in voice_data or "ok bye" in voice_data or "stop" in voice_data or "exit" in voice_data:
        speaky('your personal assistant snoopy  is shutting down,Good bye sir')
        exit()

    if 'time' in voice_data:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speaky(f"the time is {time}")

    elif 'who are you' in voice_data or 'what can you do' in voice_data or 'introduce yourself ' in voice_data:
        speaky('hello ,I am snoopy version 1 point O your personal assistant. I am programmed to minor tasks like'
               'opening youtube,google chrome, gmail ,predict time,take a photo,search wikipedia,predict weather'
               'In different cities,!')

    elif "who made you" in voice_data or "who created you" in voice_data or "who discovered you" in voice_data:
        speaky("I was built by speaky team ")

    elif 'news' in voice_data or "tell me news" in voice_data or "last news" in voice_data:
        news = webbrowser.open_new_tab("https://www.jordantimes.com/")
        speaky('Here are some headlines from the jordan Times,Happy reading')

    elif 'play music' in voice_data or 'change music' in voice_data:
        speaky('Here are your favorites enjoy it')
        music_dir = "D:\music"
        songs = os.listdir(music_dir)
        n = random.randint(0, 2)
        playmusic(music_dir + "\\" + songs[n])
    elif 'enough' in voice_data:
        speaky("Stopping playback.")
        stopmusic()


def playmusic(song):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()


def stopmusic():
    mixer.music.stop()


time.sleep(1)
if hour >= 0 and hour <= 12:
    speaky(f"Good Morning ! {person_obj.name}")
elif hour >= 12 and hour <= 18:
    speaky("Good Afternoon " + {person_obj.name})
else:
    speaky("Good Evening !" + {person_obj.name})
speaky("your assistant is ready to go , im here to serve you ")

while 1:
    voice_data = record_audio()
    respond(voice_data)
    Name(voice_data)








