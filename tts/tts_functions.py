import azure.cognitiveservices.speech as speechsdk
import simpleaudio as sa

speech_config = speechsdk.SpeechConfig(
    subscription='44d7d58744334bea8b7c72de640ed3e3', region='southeastasia')
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)


def speakText(text):
    speech_config.speech_synthesis_voice_name = "fr-FR-JeromeNeura"
    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config)
    sa.WaveObject.from_wave_file("./tts/ring.wav").play().wait_done()
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()


def speakTextSSML(text):  #change voice and style in tts_voice_config.xml
    '''
    Speak text using configurations in the tts_voice_config.xml file
    can be used to change the voice and style of the speaker
    '''
    if not text:
        return
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,
                                              audio_config=audio_config)
    ssml_string = open("./tts/tts_voice_config.xml", "r").read()
    ssml_string = ssml_string.replace('TEXT', text)
    # sa.WaveObject.from_wave_file("./tts/ring.wav").play().wait_done()
    sa.WaveObject.from_wave_file("./tts/ring.wav").play()
    result = synthesizer.speak_ssml_async(ssml_string).get()


if __name__ == "__main__":
    speakTextSSML()
    pass