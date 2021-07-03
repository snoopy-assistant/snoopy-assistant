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
engine.setProperty('voice','voices[0].id')
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
print('Loading your AI personal assistant G-One')
speak("Loading your AI personal assistant G-One")
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

        elif 'news' in  statement:
            news = webbrowser.open_new_tab('https://timesofindia.indiatimes.com/home/headlines')
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'search' in statement:
            statement = statement.replace('search','')
            webbrowser.open_new_tab(statement)
            time.sleep(5)



























