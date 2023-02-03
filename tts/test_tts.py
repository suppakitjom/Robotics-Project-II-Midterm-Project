import requests

tts_url = 'http://localhost:5001/tts'
tts_url_ubuntu = 'http://10.211.55.5:5001/tts'


def speak(text):
    r = requests.post(tts_url_ubuntu, json={'text': text})


if __name__ == "__main__":
    speak("")
    pass