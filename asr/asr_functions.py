import speech_recognition as sr
from pydub import AudioSegment
import io
import os


def listen():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Say something!")
        audio = r.listen(source)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Recognizing...")

        # TODO somehow whisper is having a permission problem. check back later
        # results = r.recognize_whisper(audio, model="tiny.en")
        results = r.recognize_google(audio, language="en-US")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(results)
    # return the text recognized
    return results



