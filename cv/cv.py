from flask import Flask

app = Flask(__name__)


@app.route('/cv', methods=['POST'])
def getRecognizedPeople():
    #extract the recognized people from the recognized.txt
    recognized = []
    with open("recognized.txt", "r") as f:
        for line in f:
            recognized.append(line.strip())
    return {'recognized': recognized}


app.run(host='localhost', port=5000)
