from greeting import speaky, record_audio
import pyttsx3
import speech_recognition as sr
import smtplib
from twilio.rest import Client
import googletrans
from googletrans import Translator


# Send E-mail by Gmail::

def send_mail():
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    sender_mail_id = 'snoopy.assistant@gmail.com'
    password = 'ayman123456'
    receiver_mail_id = 'abualneaf16@gmail.com'

    smtp.starttls()
    smtp.login(sender_mail_id, password)

    speaky('sure I will send an e-mail')
    subject = record_audio('what is the message subject ? ')
    body = record_audio('what is the message body ? ')

    massage = f'Subject: {subject}\n\n{body}'
    speaky('Sending Mail ...')
    smtp.sendmail(sender_mail_id, receiver_mail_id, massage)

    smtp.quit()
    speaky('Mail sent Successfully ...')


# Send SMS ::
def send_sms():
    account_sid = 'AC352d0cd10eeb57e043636def3c59e606'
    token = 'dfbf16707550e8482ccf9424e9c99451'

    client = Client(account_sid, token)

    message = client.messages.create(from_='+18102029307', to='+962798152307', body='Hello Ayman !!')

    print(message.sid)
    speaky('message sent successfully')


def sender(voice_data):
    if 'send mail' in voice_data or 'email' in voice_data:
        send_mail()

    if "sms" in voice_data or 'send massege' in voice_data:
        send_sms()
