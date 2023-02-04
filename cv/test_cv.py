import requests

cv_url = 'http://localhost:5000/cv'
cv_url_windows = 'http://172.20.10.2/5000/cv'


def getRecognizedPeople():
    r = requests.get(cv_url)
    return r.json()


if __name__ == "__main__":
    print(getRecognizedPeople()['recognized'])
    pass