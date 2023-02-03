import azure.cognitiveservices.speech as speechsdk
from flask import Flask, request
import simpleaudio as sa

app = Flask(__name__)

speech_config = speechsdk.SpeechConfig(
    subscription='44d7d58744334bea8b7c72de640ed3e3', region='southeastasia')
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# @app.route("/")
# def home():
#     return "home"


@app.route('/ttsbasic', methods=['POST'])
def speakText():
    body = request.get_json()
    text = body['text']
    speech_config.speech_synthesis_voice_name = "fr-FR-JeromeNeura"
    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config)
    sa.WaveObject.from_wave_file("ring.wav").play().wait_done()
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    return []


@app.route('/tts', methods=['POST'])
def speakTextSSML():  #change voice and style in tts_voice_config.xml
    body = request.get_json()
    text = body['text']
    if not text:
        text = 'An Unknown Person is at the door. Would you like to let them in?'
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,
                                              audio_config=audio_config)
    print('Input text --->', text)
    ssml_string = open("tts_voice_config.xml", "r").read()
    ssml_string = ssml_string.replace('TEXT', text)
    sa.WaveObject.from_wave_file("ring.wav").play().wait_done()
    result = synthesizer.speak_ssml_async(ssml_string).get()
    return []


app.run(host='localhost', port=5001)

if __name__ == "__main__":
    speakTextSSML()
    pass