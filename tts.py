import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(
    subscription='44d7d58744334bea8b7c72de640ed3e3', region='southeastasia')
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)


def speakText(text):

    speech_config.speech_synthesis_voice_name = "fr-FR-JeromeNeura"
    speech_config.set_profanity = 2

    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config)
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()


def speakTextSSML(text=None):
    defaultresponse = 'An Unknown Person is at the door. Would you like to let them in?'
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,
                                              audio_config=audio_config)

    ssml_string = open("tts_voice_config.xml", "r").read()
    if text:
        ssml_string = ssml_string.replace('TEXT', text)
    else:
        ssml_string = ssml_string.replace('TEXT', defaultresponse)

    result = synthesizer.speak_ssml_async(ssml_string).get()
    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file("tts_temp.wav")


if __name__ == "__main__":
    speakTextSSML()
