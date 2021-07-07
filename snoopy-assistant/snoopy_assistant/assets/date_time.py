from greeting import speaky, record_audio
import speech_recognition as sr
import requests
import datetime


def weatherTime(voice_data):
  

     if 'time' in voice_data:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speaky(f"the time is {current_time}")


     if 'today' in voice_data or 'day' in voice_data :

            the_day = datetime.datetime.today().weekday() + 1

            day_obj = { 1: 'Monday', 2: 'Tuesday',
                        3: 'Wednesday', 4: 'Thursday',
                        5: 'Friday', 6: 'Saturday',
                        7: 'Sunday' }
            if the_day in day_obj.keys():
                day_of_today = day_obj[the_day]

                speaky(f"today is {day_of_today}")

     elif "date" in  voice_data :
            date= datetime.date.today()
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
       
       if  "write a note" in voice_data:
         
              speaky("What should I write please ?")
              my_note =record_audio()
              file = open('text.txt', 'w')
              speaky("should I write date and time for you ?")
              command = record_audio()
              if 'yes' in command or 'sure' in command:
                     str_time = str(datetime.datetime.now())
                     file.write(str_time)
                     file.write(":")
                     file.write(my_note)
                     speaky("done")
              else:
                     file.write(my_note)
                     speaky("done")
                
       elif "show me" in voice_data:
            speaky("done")
            file = open("text.txt", "r")
            print(file.read())

