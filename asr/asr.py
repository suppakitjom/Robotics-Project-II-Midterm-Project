import speech_recognition as sr
from pydub import AudioSegment
import io
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/stt", methods=['GET'])
def listen():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        # clear terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Say something!")
        global audio
        audio = r.listen(source)
        results = r.recognize_whisper(audio, model="tiny.en")
    return results


app.run(host='localhost', port=5002)

if __name__ == "__main__":
    text = listen()
    data = io.BytesIO(audio.get_wav_data())
    audio_clip = AudioSegment.from_file(data)
    audio_clip.export('temp.wav', format="wav")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(text)
    pass
