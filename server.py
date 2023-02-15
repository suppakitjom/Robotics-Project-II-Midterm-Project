'''
server to handle requests from Jetson Nano
will receive a list of known people in front of the camera
will let the user know who is in front of the camera using tts
will receive the command from user using asr
will process the command using rasa
and will act accordingly (send command to Jetson Nano)
'''

from flask import Flask, request
import requests as req

app = Flask(__name__)
from tts.tts_functions import speakTextSSML, speakText
from asr.asr_functions import listen
from rasa.rasa_functions import process_command


@app.route('/')
def receive_known_people():
    # body = request.get_json()
    # names = body['recognized']
    # names = names.split(',')
    names = 'Jom Punn Neno Kitty Roong'.split()
    text = 'An Unknown Person is at the door. Would you like to let them in?'
    if len(names) == 1:
        text = f'Hello sir. {names[0]} is at the door. Would you like to let them in?'
    elif len(names) > 1:
        temp = ', '.join(names[:-1])
        text = f'Hello sir. {temp}and {names[-1]} are at the door. Would you like to let them in?'
    speakTextSSML(text)

    command = listen()
    while not command:
        speakTextSSML('Sorry, I did not get that. Please try again.')
        command = listen()

    intent, confidence = process_command(command)
    #print intent and confidence for debugging
    print(intent, confidence)
    if intent == 'allow' and confidence > 0.95:
        speakTextSSML('Okay, I will let them in now.')
        # TODO send command to Jetson Nano to open the door - To be added
    elif intent == 'deny' and confidence > 0.95:
        speakTextSSML('Okay, I will not let them in.')


if __name__ == '__main__':
    receive_known_people()