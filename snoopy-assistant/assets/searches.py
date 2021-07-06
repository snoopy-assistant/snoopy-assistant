import datetime
import tkinter
import webbrowser

import speech_recognition as sr
from urllib import request
import json
import pyttsx3
import wikipedia
import time







#-----------------------------------------------------jokes

url = 'http://official-joke-api.appspot.com/jokes/random'
r = request.urlopen(url)
data = r.read()
jsonData = json.loads(data)
print(jsonData)

#___________________________________________________________________________________
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', rate-20)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        audio = r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f'user said:{statement}\n')
        except Exception as e:
            speak('Pardon me, please say that again')
            return 'None'
        return statement
print('Loading your dog personal assistant snoopy')
speak("Loading your dog personal assistant snoopy")
wishMe()
speak('THANK YOU BEAUTIFUL CROWD Big thanks to everyone who joined our Livestream Thank you for your Lovely Feedback and your orders and Special thanks to Mr.Ahmad and the instructional team')








def talk():


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue


        if 'joke' in statement:
            speak(jsonData['setup'] + jsonData['punchline'])


        if 'goodbye' in statement or 'bye' in statement or 'stop' in statement:
            speak('Ok man relax I am a good dog')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace('wikipedia','')
            results = wikipedia.summary(statement, sentences=3)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab('https://www.youtube.com')
            speak('youtube is open now')

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'open facebook' in statement:
            webbrowser.open_new_tab("facebook.com")
            speak("facebook is open now")
            time.sleep(5)


        elif 'open discord' in statement:
            webbrowser.open_new_tab("https://discord.com/")
            speak("discord is open now")
            time.sleep(5)

        elif 'news' in  statement:
            news = webbrowser.open_new_tab('https://timesofindia.indiatimes.com/home/headlines')
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'search' in statement:
            statement = statement.replace('search','')
            webbrowser.open_new_tab(f'https://www.google.jo/search?q={statement}&sxsrf=ALeKk03Qm_B-cTbf7gsRTNFipWrVsqZk5A%3A1625323098676&source=hp&ei=WnbgYLvyJqCPhbIP5Z-woAg&iflsig=AINFCbYAAAAAYOCEanVOpdEeam8Lq3lP_kODEmW2Uw5V&oq=&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJ1AAWABg3SVoAXAAeACAAQCIAQCSAQCYAQCqAQdnd3Mtd2l6sAEK&sclient=gws-wiz')
            time.sleep(5)


#------------------------------------------------------gui
import tkinter as tk
from PIL import Image
root = tk.Tk()
root.title('SNOOPY ')


root.iconbitmap('snoopy.ico')
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


def update(ind):
    ind += 1
    label.configure(image=frames)
    root.after(100, update, ind)


def open():
    newWindow = tk.Toplevel(root)
    # newWindow.iconbitmap('D:/snoopy.ico')
    newWindow.title("features")
    newWindow.geometry("300x350")
    label1 = tk.Listbox(newWindow, height=200, width=500, bg='black', fg="white", activestyle='dotbox',font = "Helvetica 16 bold italic")
    label1.insert(1, "Snoopy present to you ")
    label1.insert(2, "                        ")
    label1.insert(3, "1- tell a joke ")
    label1.insert(4, "2- send emails ")
    label1.insert(5, "3- send SMS  ")
    label1.insert(6, "4- find location ")
    label1.insert(7, "5- open browser ")
    label1.pack()
    newWindow.mainloop()



# talk = respond(voice_data)
features = tk.Button(height=1, width=10, text="features", command=open, bg='#f24b4b', fg='#f2f2f2')
features.config(font=("Arial", 12))
features.place(x=50, y=575)

talk = tk.Button(height=1, width=10, text="Talk ", command=talk(), bg='#f24b4b', fg='#f2f2f2')
talk.config(font=("Arial", 12))
talk.place(x=200, y=575)

stop = tk.Button(height=1, width=10, text="Stop",bg='#f24b4b', fg='#f2f2f2')
stop.config(font=("Arial", 12))
stop.place(x=350, y=575)

label = tk.Label(height=200, width=300, bg="black").pack()
root.mainloop()




































