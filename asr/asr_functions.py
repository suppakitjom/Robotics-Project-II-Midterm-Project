import speech_recognition as sr
import os
import time


def listen():
    r = sr.Recognizer()
    r.energy_threshold = 300  #4500 works well in MI lab
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Say something!")
        audio = r.listen(source)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Recognizing...")

        # TODO somehow whisper is having a permission problem. check back later
        start = time.time()
        try:
            # Rasa, faster and more accurate with longer clips
            results = r.recognize_whisper(audio, model="tiny.en")
            # Google, fast with short phrases FUCKS IT ALL UP WITH LONGER CLIPS
            # results = r.recognize_google(audio)
        except:
            print("Sorry, I did not get that. Please try again.")
            return None

        os.system('cls' if os.name == 'nt' else 'clear')
        end = time.time()
        print(f"Time taken to transcribe: {end-start:.2f} seconds")
        print(f"Transcribed: {results}")
        with open("temp.wav", "wb") as f:
            f.write(audio.get_wav_data())
        return results


if __name__ == "__main__":
    print(listen())
    pass
