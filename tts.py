import azure.cognitiveservices.speech as speechsdk


def speakText(text):
    speech_config = speechsdk.SpeechConfig(
        subscription='44d7d58744334bea8b7c72de640ed3e3',
        region='southeastasia')
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    speech_config.speech_synthesis_voice_name = "en-US-RogerNeural"

    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config)

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()