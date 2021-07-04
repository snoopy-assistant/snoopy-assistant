import datetime
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








if __name__=='__main__':


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






























