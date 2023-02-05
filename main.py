# TODO get list of recognized faces from Jetson Nano - To be added

recognized = ['Jom', 'Neno', 'Punn', 'Kitty', 'Roong']  # example
# recognized = ['Jom']

from tts.tts_functions import speakText, speakTextSSML

if len(recognized) == 1:
    text = f'Hello sir. {recognized[0]} is at the door. Would you like to let them in?'
elif len(recognized) > 1:
    temp = ', '.join(recognized[:-1])
    text = f'Hello sir. {temp}and {recognized[-1]} are at the door. Would you like to let them in?'
else:
    text = ''

speakTextSSML(text)

from asr.asr_functions import listen

text = listen()
while not text:
    speakTextSSML('Sorry, I did not get that. Please try again.')
    text = listen()

import requests
import json

rasa_url = 'http://localhost:5005/model/parse'
payload = {"text": text}
r = requests.post(rasa_url, json=payload)
intent = r.json()['intent']['name']
confidence = r.json()['intent']['confidence']

while (intent not in ['allow', 'deny']) and (confidence < 0.7):
    speakTextSSML('Sorry, I did not get that. Please try again.')
    text = listen()
    payload = {"text": text}
    r = requests.post(rasa_url, json=payload)
    intent = r.json()['intent']['name']
    confidence = r.json()['intent']['confidence']

with open("./rasa/.rasarasa_test_temp.json", "w") as f:
    f.write(json.dumps(r.json(), indent=4))

if intent == 'allow' and confidence > 0.95:
    speakTextSSML('Okay, I will let them in now.')
    # TODO send command to Jetson Nano to open the door - To be added
elif intent == 'deny' and confidence > 0.95:
    speakTextSSML('Okay, I will not let them in.')
