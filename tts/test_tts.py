import requests

tts_url = 'http://localhost:5001/tts'
tts_url_ubuntu = 'http://10.211.55.5:5001/tts'


def speak(text):
    r = requests.put(tts_url, json={'text': text})


if __name__ == "__main__":
    speak("AH SHIT! AN ERROR!")
    pass