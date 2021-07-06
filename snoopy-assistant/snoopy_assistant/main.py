import datetime
import json
import os
import random
import smtplib
import time
import tkinter as tk
from urllib import request
import webbrowser
import requests
import speech_recognition as sr
import wikipedia
from PIL import Image
from gtts import gTTS
from playsound import playsound
from pygame import mixer
from twilio.rest import Client

###################################################### helper functions & classs  ##############################################################################

root = tk.Tk()
root.iconbitmap('voice.ico')
root.geometry('500x700+200+10')

file = "snoopy.gif"
info = Image.open(file)
frames = info.n_frames

im = [tk.PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]
count = 0
anim = None


def animation(count):
    global anim
    im2 = im[count]
    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50, lambda: animation(count))


gif_label = tk.Label(root, image="", bg="black")
gif_label.pack()

animation(5)

url = 'http://official-joke-api.appspot.com/jokes/random'
r = request.urlopen(url)
data = r.read()
jsonData = json.loads(data)


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

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        print('Listening ...')
        if ask:
            speaky(ask)
        audio = r.listen(source, timeout=5)
        voice_data = ''
        try:
            print('Recognizing... ')

            voice_data = r.recognize_google(audio)
            print(voice_data)

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


def send_mail():
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    sender_mail_id = 'snoopy.assistant@gmail.com'
    password = 'ayman123456'
    receiver_mail_id = 'abualneaf16@gmail.com'

    smtp.starttls()
    smtp.login(sender_mail_id, password)

    speaky('sure I will send an e-mail')
    subject = record_audio('what is the message subject ? ')
    body = record_audio('what is the message body ? ')

    massage = f'Subject: {subject}\n\n{body}'
    speaky('Sending Mail ...')
    smtp.sendmail(sender_mail_id, receiver_mail_id, massage)

    smtp.quit()
    speaky('Mail sent Successfully ...')


# Send SMS ::
def send_sms():
    account_sid = 'AC352d0cd10eeb57e043636def3c59e606'
    token = 'dfbf16707550e8482ccf9424e9c99451'

    client = Client(account_sid, token)

    message = client.messages.create(from_='+18102029307', to='+962798152307', body='Hello Ayman !!')

    print(message.sid)
    speaky('message sent successfully')


################################################ All features ########################################################################


def respond(voice_data):
    if "what is your name" in voice_data or "what's your name" in voice_data or "tell me your name" in voice_data:

        if person_obj.name:
            speaky(f"My name is {asis_obj.name}, {person_obj.name}")
        else:
            speaky(f"My name is {asis_obj.name}. what's your name?")
    if "my name is" in voice_data:
        person_name = voice_data.split("is")[-1].strip()
        speaky("okay, i will remember that " + person_name)
        speaky('how your day going?' + person_name)
        person_obj.setName(person_name)

    if 'hey' in voice_data or 'hi ' in voice_data or 'hello ' in voice_data:
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

    elif 'who are you' in voice_data or 'what can you do' in voice_data or 'introduce yourself ' in voice_data:
        speaky('hello ,I am snoopy version 1 point O your personal assistant. I am programmed to minor tasks like'
               'opening youtube,google chrome, gmail ,predict time,play music,find location,search wikipedia,predict weather'
               'In different cities,!')

    elif "who made you" in voice_data or "who created you" in voice_data or "who discovered you" in voice_data:
        speaky("I was built by speaky team ")


    elif 'play music' in voice_data or 'change music' in voice_data:
        speaky('Here are your favorites enjoy it')
        music_dir = "D:\music"
        songs = os.listdir(music_dir)
        n = random.randint(0, 2)
        playmusic(music_dir + "\\" + songs[n])
    elif 'enough' in voice_data:
        speaky("Stopping playback.")
        stopmusic()
    if 'time' in voice_data:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speaky(f"the time is {current_time}")

    if 'today' in voice_data or 'day' in voice_data:

        the_day = datetime.datetime.today().weekday() + 1

        day_obj = {1: 'Monday', 2: 'Tuesday',
                   3: 'Wednesday', 4: 'Thursday',
                   5: 'Friday', 6: 'Saturday',
                   7: 'Sunday'}
        if the_day in day_obj.keys():
            day_of_today = day_obj[the_day]

            speaky(f"today is {day_of_today}")
    elif "date" in voice_data:
        date = datetime.date.today()
        speaky(f"the date is {date}")

    if "weather" in voice_data:
        city_name = record_audio("what is the city name")
        api_key = "0b3f253b870f4c61b104c97b388d28b6"
        base_url = f"https://api.weatherbit.io/v2.0/forecast/daily?city={city_name}&key={api_key}"

        response = requests.get(base_url)
        data = response.json()
        description = data["data"][0]["weather"]["description"]
        temperature = data["data"][0]["high_temp"]
        speaky(f"{description} in {city_name}  and the temperature is {temperature} \n")
    if 'joke' in voice_data:
        speaky(jsonData['setup'] + jsonData['punchline'] + 'HAHAHAHAHA')
    if 'wikipedia' in voice_data:
        speaky('Searching Wikipedia...')
        statement = voice_data.replace('wikipedia', '')
        results = wikipedia.summary(statement, sentences=3)
        speaky('According to Wikipedia')
        speaky(results)
    elif 'open youtube' in voice_data:
        webbrowser.open_new_tab('https://www.youtube.com')
        speaky('youtube is open now')
    elif 'open google' in voice_data:
        webbrowser.open_new_tab("https://www.google.com")
        speaky("Google chrome is open now")
    elif 'open gmail' in voice_data:
        webbrowser.open_new_tab("gmail.com")
        speaky("Google Mail open now")
    elif 'open facebook' in voice_data:
        webbrowser.open_new_tab("facebook.com")
        speaky("facebook is open now")
    elif 'open discord' in voice_data:
        webbrowser.open_new_tab("https://discord.com/")
        speaky("discord is open now")
    elif 'news' in voice_data or "tell me news" in voice_data or "last news" in voice_data:
        news = webbrowser.open_new_tab("https://www.jordantimes.com/")
        speaky('Here are some headlines from the jordan Times,Happy reading')
    if 'search' in voice_data:
        search = record_audio('what do you want search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speaky('Here is what I found for ' + search)
    if 'send mail' in voice_data or 'email' in voice_data:
        send_mail()
    if "sms" in voice_data or 'send massege' in voice_data:
        send_sms()
    if "bye" in voice_data or "ok bye" in voice_data or "stop" in voice_data or "exit" in voice_data:
        speaky('your personal assistant snoopy  is shutting down,Good bye sir')
        exit()


def stop():
    speaky('your personal assistant snoopy is shutting down,Good bye sir')
    exit()


def playmusic(song):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()


def stopmusic():
    mixer.music.stop()


time.sleep(1)



def start_point():


    if hour >= 0 and hour <= 12:
        speaky(f"Good Morning ! ")
    elif hour >= 12 and hour <= 18:
        speaky("Good Afternoon ")
    else:
        speaky("Good Evening !")
    speaky("your assistant is ready to go , im here to serve you ")
    while 1:
        voice_data = record_audio()
        respond(voice_data)


#################################################GUI###############################################################


def update(ind):
    ind += 1
    label.configure(image=frame)
    root.after(100, update, ind)


def open():
    newWindow = tk.Toplevel(root)
    newWindow.iconbitmap('voice.ico')
    newWindow.title("features")
    newWindow.geometry("300x350")
    label1 = tk.Listbox(newWindow, height=200, width=500, bg='black', fg="white", activestyle='dotbox',
                        font="Helvetica 16 bold italic")
    label1.insert(1, "Snoopy present to you ")
    label1.insert(2, "                        ")
    label1.insert(3, "1- tell a joke ")
    label1.insert(4, "2- send emails ")
    label1.insert(5, "3- send SMS  ")
    label1.insert(6, "4- find location ")
    label1.insert(7, "5- open browser ")
    label1.pack()
    newWindow.mainloop()


root.title('SNOOPY ')
# talk = respond(voice_data)
features = tk.Button(height=1, width=10, text="features", command=open, bg='#f24b4b', fg='#f2f2f2')
features.config(font=("Arial", 12))
features.place(x=50, y=575)

talk = tk.Button(height=1, width=10, text="Talk ", command=start_point, bg='#f24b4b', fg='#f2f2f2')
talk.config(font=("Arial", 12))
talk.place(x=200, y=575)

stop = tk.Button(height=1, width=10, text="Stop", command=stop, bg='#f24b4b', fg='#f2f2f2')
stop.config(font=("Arial", 12))
stop.place(x=350, y=575)

label = tk.Label(height=200, width=300, bg="black").pack()
root.mainloop()




####################################################GUI##############################################################
