import requests
import os

cv_url = 'http://localhost:5000/cv'
cv_url_windows = 'http://172.20.10.2/5000/cv'
cv_url_jetson = 'http://192.168.2.2:5000/cv'


def getRecognizedPeople():
    r = requests.get(cv_url_jetson)
    return r.json()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(getRecognizedPeople()['recognized'])
    pass