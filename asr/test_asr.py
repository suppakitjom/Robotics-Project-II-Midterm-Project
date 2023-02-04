import requests

asr_url = 'http://localhost:5002/stt'


def listen():
    print('I\'m listening....')
    r = requests.get(asr_url)
    print(r.text)


if __name__ == '__main__':
    listen()
    pass