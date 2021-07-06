import pyttsx3
import speech_recognition as sr
import datetime



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

        elif "write a note" in statement:

            speak("What should I write please ?")
            my_note = take_command()
            # writing
            file = open('text.txt', 'w')
            speak("should I write date and time for you ?")
            command = take_command()
            if 'yes' in command or 'sure' in command:
                str_time = str(datetime.datetime.now())
                file.write(str_time)
                file.write(":")
                file.write(my_note)
                speak("done")
            else:
                file.write(my_note)
                speak("done")
                
        elif "show me" in statement:
            speak("done")
            # reading
            file = open("text.txt", "r")
            print(file.read())





        elif "stop" in statement:
            speak("bye and take care")
            break