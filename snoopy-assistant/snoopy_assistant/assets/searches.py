from greeting import speaky ,record_audio
import webbrowser
import speech_recognition as sr
from urllib import request
import json
import pyttsx3
import wikipedia





#-----------------------------------------------------jokes----------------------------------------------------

url = 'http://official-joke-api.appspot.com/jokes/random'
r = request.urlopen(url)
data = r.read()
jsonData = json.loads(data)
print(jsonData)

#___________________________________________________________________________________

def searching (voice_data):
        if 'joke' in voice_data:
            speaky(jsonData['setup'] + jsonData['punchline'])


        if 'wikipedia' in voice_data:
            speaky('Searching Wikipedia...')
            statement = voice_data.replace('wikipedia','')
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


























