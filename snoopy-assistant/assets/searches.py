# import speech_recognition as sr
#
import webbrowser
from urllib import request
import json
# import pyttsx3

# if 'open youtube' in statement:
# webbrowser.open_new_tab("https://www.youtube.com")
# speak("youtube is open now")
# time.sleep(5)
#
# elif 'open google' in statement:
# webbrowser.open_new_tab("https://www.google.com")
# speak("Google chrome is open now")
# time.sleep(5)
#
# elif 'open gmail' in statement:
# webbrowser.open_new_tab("gmail.com")
# speak("Google Mail open now")
# time.sleep(5)
#
#
# elif 'open facebook' in statement:
# webbrowser.open_new_tab("facebook.com")
# speak("face book is open now")
# time.sleep(5)

#-----------------------------------------------------jokes
url = 'http://official-joke-api.appspot.com/random_ten'
r = request.urlopen(url)
print(r.getcode())
data = r.read()
jsonData = json.loads(data)
# print(jsonData)
class Joke:
    def __init__(self,setup,punchline):
        self.setup = setup
        self.punchline = punchline

    def __str__(self):
        return f'setup {self.setup} punchline {self.punchline}'

jokes=[]
for j in jsonData:
    setup = j['setup']
    punchline = j['punchline']
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f'Got {len(jokes)} jokes')

for joke in jokes:
    print(joke)
    # pyttsx3.speak('joke setup')
    # pyttsx3.speak(joke.setup)
    # pyttsx3.speak('joke punchline')
    # pyttsx3.speak(joke.punchline)










