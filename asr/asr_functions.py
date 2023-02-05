import speech_recognition as sr
import os
# import whisper
import time


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
        start = time.time()
        try:
            results = r.recognize_google(audio,
                                         language="en-US")  #currently fastest
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        end = time.time()
        print(f"Time taken to transcribe: {end-start:.2f} seconds")
        return results

        # workaround with whisper
        #write audio to a WAV file
        # with open("temp.wav", "wb") as f:
        #     f.write(audio.get_wav_data())
        # model = whisper.load_model("tiny.en")
        # start = time.time()
        # results = model.transcribe('temp.wav', fp16=False, language="english")
        # end = time.time()
        # os.system('cls' if os.name == 'nt' else 'clear')
        # print(results['text'])
        # # return the text recognized
        # print(f"Time taken: {end-start:.2f} seconds")
        # return results['text']


if __name__ == "__main__":
    listen()
    pass
