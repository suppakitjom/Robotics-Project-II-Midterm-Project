import requests as req
from tts.tts_functions import speakTextSSML, speakText
from asr.asr_functions import listen


def process_command(text):
    rasa_url = 'http://localhost:5005/model/parse'
    payload = {"text": text}
    r = req.post(rasa_url, json=payload)
    intent = r.json()['intent']['name']
    confidence = r.json()['intent']['confidence']

    while (intent not in ['allow', 'deny']) or (confidence < 0.7):
        speakTextSSML('Sorry, I did not get that. Please try again.')
        text = listen()
        payload = {"text": text}
        r = req.post(rasa_url, json=payload)
        intent = r.json()['intent']['name']
        confidence = r.json()['intent']['confidence']

    return intent, confidence