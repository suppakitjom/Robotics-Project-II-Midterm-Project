'''
server to handle requests on Jetson Nano
'''

from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/cv', methods=['GET'])
def getRecognizedPeople():
    #extract the recognized people from the recognized.txt
    recognized = []
    with open("recognized.txt", "r") as f:
        for line in f:
            recognized.append(line.strip())
    return {'recognized': recognized}


app.run(host=os.getenv('JETSON_IP_ADDRESS'), port=5000)
