import requests

tts_url = 'http://localhost:5001/tts'


def speak(text):
    r = requests.post(tts_url, json={'text': text})


if __name__ == "__main__":
    speak("Hello sir. I am your personal assistant.")
    pass