import requests
import json

url = 'http://localhost:5005/model/parse'
payload = {"text": "blah blah blah"}

try:
    r = requests.post(url, json=payload)
    with open("temp.json", "w") as f:
        f.write(json.dumps(r.json(), indent=4))
    intent = r.json()['intent']['name']
    confidence = r.json()['intent']['confidence']
    print("Intent: " + intent)
    print("Confidence: " + str(confidence))
except Exception as e:
    print(e)
