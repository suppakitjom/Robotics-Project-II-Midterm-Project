import requests
import json

rasa_url = 'http://localhost:5005/model/parse'
rasa_url_windows = 'http://172.20.10.2:5005/model/parse'
payload = {"text": "please let them in"}

try:
    r = requests.post(rasa_url_windows, json=payload)
    with open("rasa_test_temp.json", "w") as f:
        f.write(json.dumps(r.json(), indent=4))
    intent = r.json()['intent']['name']
    confidence = r.json()['intent']['confidence']
    print("Intent: " + intent)
    print("Confidence: " + str(confidence))
except Exception as e:
    print(e)
