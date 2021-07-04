import pyttsx3
import speech_recognition as sr
import requests
import datetime
import json


engin=pyttsx3.init('sapi5')
voices=engin.getProperty('voices')
engin.setProperty('voice','voices[0].id')

def speak(txt):

    """
    this function which
    converts text to speech

    """
    engin.say(txt)
    engin.runAndWait()

def take_command():

    """
    this function which
    take command from the user
    converts speech to text

    """
    command=sr.Recognizer()

    with sr.Microphone() as sourc:
        print("Im Listen now........")
        Audiu=command.listen(sourc)

        try:
            statment=command.recognize_google(Audiu,language='en')
            print(f"the user say => {statment}\n \n")

        except Exception as error:
            speak("please say again")
            return "None"
        return statment

speak("please wait")

if __name__ == '__main__':


    while True :
        speak("Tell me how can I help you ?")
        statement = take_command().lower()
        if statement == 0:
            continue

        elif 'time' in statement:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {current_time}")


        elif 'today' in statement or 'day' in statement :

            the_day = datetime.datetime.today().weekday() + 1

            day_obj = { 1: 'Monday', 2: 'Tuesday',
                        3: 'Wednesday', 4: 'Thursday',
                        5: 'Friday', 6: 'Saturday',
                        7: 'Sunday' }
            if the_day in day_obj.keys():
                day_of_today = day_obj[the_day]

                speak(f"today is {day_of_today}")




        elif "weather" in statement:

            speak("what is the city name")
            city_name = take_command()
            api_key = "0b3f253b870f4c61b104c97b388d28b6"
            base_url = f"https://api.weatherbit.io/v2.0/forecast/daily?city={city_name}&key={api_key}"

            response = requests.get(base_url)
            data = response.json()
            description = data["data"][0]["weather"]["description"]
            temperature = data["data"][0]["high_temp"]
            speak(f"{description} in {city_name}  and the temperature is {temperature} \n")




        elif "stop" in statement:
            speak("bye and take care")
            break
