import pyttsx3
import speech_recognition as sr
import smtplib
from twilio.rest import Client
import googletrans
from googletrans import Translator


# Voice Say ::
def speak(sentence):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)  # this is male voice
    engine.setProperty('rate', 150)  # the speed of talk
    engine.setProperty('voice', voices[3].id)  # this is female voice
    engine.say(sentence)
    print(f'Snoopy: {sentence}')
    engine.runAndWait()
    return sentence


#  Talk to assistant ::
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening ...')
        # r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=2)
    try:
        print('Recognizing... ')
        query = r.recognize_google(audio, language='en')
        # print(f'User Said {query}\n')

    except Exception as e:
        speak('Say Again please ...')
        take_command()
    query = query.lower()
    print(f'you say: {query}')
    return query


# Send E-mail by Gmail::
def send_mail():
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    sender_mail_id = 'snoopy.assistant@gmail.com'
    password = 'ayman123456'
    receiver_mail_id = 'abualneaf16@gmail.com'

    smtp.starttls()  # start connecting with gmail
    smtp.login(sender_mail_id, password)  # login to gmail account

    speak('sure I will send an e-mail')
    speak('what is the message subject ?')
    subject = take_command()

    speak('what is the message body ?')
    body = take_command()

    massage = f'Subject: {subject}\n\n{body}'
    speak('Sending Mail ...')
    smtp.sendmail(sender_mail_id, receiver_mail_id, massage)

    smtp.quit()
    speak('Mail sent Successfully ...')


# Send SMS ::
def send_sms():
    account_sid = 'AC352d0cd10eeb57e043636def3c59e606'
    token = 'dfbf16707550e8482ccf9424e9c99451'

    client = Client(account_sid, token)

    message = client.messages.create(from_='+18102029307', to='+962798152307', body='Hello Ayman !!')

    print(message.sid)
    speak('message sent successfully')

