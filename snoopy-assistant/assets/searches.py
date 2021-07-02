import datetime
import speech_recognition as sr
from urllib import request
import json
import pyttsx3


#-----------------------------------------------------jokes
# url = 'http://official-joke-api.appspot.com/random_ten'
# r = request.urlopen(url)
# print(r.getcode())
# data = r.read()
# jsonData = json.loads(data)
# # print(jsonData)
# class Joke:
#     def __init__(self,setup,punchline):
#         self.setup = setup
#         self.punchline = punchline
#
#     def __str__(self):
#         return f'setup {self.setup} punchline {self.punchline}'
#
# jokes=[]
# for j in jsonData:
#     setup = j['setup']
#     punchline = j['punchline']
#     joke = Joke(setup, punchline)
#     jokes.append(joke)
#
# print(f'Got {len(jokes)} jokes')
#
# for joke in jokes:
#     print(joke)
#
#     pyttsx3.speak(joke.setup)
#     pyttsx3.speak('joke punchline')
#     pyttsx3.speak(joke.punchline)
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

        if "joke" in statement or "ok bye" in statement or "stop" in statement:
            speak('python is easy')
            print('python is easy')
            break













