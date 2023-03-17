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

from cv.cv_utility import getRecognizedPeople
from tts.tts_functions import speakTextSSML, speakText
from asr.asr_functions import listen
from rasa.rasa_functions import process_command


@app.route('/main', methods=['POST'])
def main():
    # retrieve names of known people in front of camera
    # and store it in a list
    body = request.get_json()
    names = body['recognized']  #.split(', ')
    # names = getRecognizedPeople()['recognized']
    # names = 'Jom Punn Neno Kitty Roong'.split()

    # generate text to be spoken and speak it
    text = 'An Unknown Person is at the door. Would you like to let them in?'
    if len(names) == 1:
        text = f'Hello sir. {names[0]} is at the door. Would you like to let them in?'
    elif len(names) > 1:
        temp = ', '.join(names[:-1])
        text = f'Hello sir. {temp}and {names[-1]} are at the door. Would you like to let them in?'
    speakTextSSML(text)

    # listen to user's command
    command = listen()
    while not command:  # if no command is detected, ask user to repeat themself
        speakTextSSML('Sorry, I did not get that. Please try again.')
        command = listen()

    # process the command using rasa
    intent, confidence = process_command(command)
    #print intent and confidence for debugging
    print(intent, confidence)

    # act according to the user's intent
    if intent == 'allow' and confidence > 0.95:
        speakTextSSML('Okay, I will let them in now.')
        # TODO send command to Jetson Nano to open the door
        # JETSON_IP_ADDRESS = '172.20.10.2' #moj
        JETSON_IP_ADDRESS = '192.168.2.2'  #lan
        req.get(url=JETSON_IP_ADDRESS + '/open_door')
    elif intent == 'deny' and confidence > 0.95:
        speakTextSSML('Okay, I will not let them in.')
    return 'DONE'


if __name__ == '__main__':
    # main()
    # app.run('172.20.10.4', port=5001)
    app.run('192.168.2.1', port=5001)