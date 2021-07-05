from ibm_watson import LanguageTranslatorV3, TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import pyttsx3
import speech_recognition as sr


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


def speak(sentence):
    engine = pyttsx3.init(driverName='sapi5')
    voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)  # this is male voice
    engine.setProperty('rate', 120)  # the speed of talk
    engine.setProperty('voice', voices[1].id)  # this is female voice
    engine.say(sentence)
    print(f'Snoopy: {sentence}')
    engine.runAndWait()
    return sentence


def translator(to_lan):
    apikey = 'CbQrcjaIiTgW3EEX9UXuV3bF80oY8SHx5wVfPwC2360c'
    url = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/2b0ceff0-5a9e-4270-a6c6-4b5ef09ad228'

    authenticator = IAMAuthenticator(apikey)
    lt = LanguageTranslatorV3(version='2021-07-03', authenticator=authenticator)
    lt.set_service_url(url)
    text = take_command()
    lan = lt.identify(text).get_result()
    from_lan = lan['languages'][0]['language']
    print(from_lan)
    print(type(from_lan))
    print('translating...')
    translation = lt.translate(text=text, model_id=f'{from_lan}-{to_lan}').get_result()
    result = translation['translations'][0]['translation']
    print(result)
    return result


def speak_lan(sentence):
    speaker_lan = { 
        'Arabic': ['ar-MS_OmarVoice'],
        'Brazilian': ['pt-BR_IsabelaV3Voice'],
        'Chinese': ['zh-CN_LiNaVoice', 'zh-CN_WangWeiVoice', 'zh-CN_ZhangJingVoice'],
        'Dutch': ['nl-NL_EmmaVoice', 'nl-NL_LiamVoice'],
        'English': ['en-AU_CraigVoice', 'en-AU_MadisonVoice', 'en-GB_CharlotteV3Voice', 'en-GB_JamesV3Voice',
                    'en-GB_KateV3Voice', 'en-US_AllisonV3Voice', 'en-US_EmilyV3Voice', 'en-US_HenryV3Voice',
                    'en-US_KevinV3Voice', 'en-US_LisaV3Voice', 'en-US_MichaelV3Voice', 'en-US_OliviaV3Voice'],
        'French': ['fr-FR_NicolasV3Voice', 'fr-FR_ReneeV3Voice', 'fr-FR_LouiseV3Voice'],
        'German': ['de-DE_BirgitV3Voice', 'de-DE_DieterV3Voice', 'de-DE_ErikaV3Voice'],
        'Italian': ['it-IT_FrancescaV3Voice'],
        'Japanese': ['ja-JP_EmiV3Voice'],
        'Korean': ['ko-KR_HyunjunVoice', 'ko-KR_SiWooVoice', 'ko-KR_YoungmiVoice', 'ko-KR_YunaVoice'],
        'Spanish': ['es-ES_EnriqueV3Voice', 'es-ES_LauraV3Voice', 'es-LA_SofiaV3Voice', 'es-US_SofiaV3Voice']
    }

    ttsapikey = '0BcG-ixhjWBmFfp6joSLiN6UVsXHl7xN35lO7O7kRpaP'
    ttsurl = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/509e73e9-bb97-40b5-8d27-574ac0f6d4dc'
    # Authenticate
    ttsauthenticator = IAMAuthenticator(ttsapikey)
    tts = TextToSpeechV1(authenticator=ttsauthenticator)
    tts.set_service_url(ttsurl)
    text = sentence
    with open('help.mp3', 'wb') as audio_file:

        res = tts.synthesize(text, accept='audio/mp3', voice=speaker_lan['German'][1]).get_result()
        audio_file.write(res.content)


if __name__ == '__main__':
    speak_lan(translator('de'))