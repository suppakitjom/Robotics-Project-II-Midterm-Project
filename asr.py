import speech_recognition as sr
from pydub import AudioSegment
import io
import os

r = sr.Recognizer()
r.energy_threshold = 400
r.dynamic_energy_threshold = True

with sr.Microphone() as source:
    # clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Say something!")
    audio = r.listen(source)

data = io.BytesIO(audio.get_wav_data())
audio_clip = AudioSegment.from_file(data)
audio_clip.export('temp.wav', format="wav")

results = r.recognize_whisper(audio, model="tiny.en")
os.system('cls' if os.name == 'nt' else 'clear')
print()
print("Predicted text:", results)
print()
