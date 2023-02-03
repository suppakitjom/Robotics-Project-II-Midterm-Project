# Robotics-Project-II-Midterm-Project

# Details

cv_url : http://localhost:5000/cv

tts_url : http://localhost:5001/tts

asr_url : http://localhost:5002/stt

rasa_url : http://localhost:5005/model/parse

## ASR (OpenAI Whisper) [GitHub](https://github.com/openai/whisper)

`cd asr`

`python asr.py`

## TTS (Microsoft Azure Text-To-Speech) [Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/index-text-to-speech)

`cd tts`

`python tts.py`

## NLU (Rasa) [Documentation](https://rasa.com/docs/rasa/)

`cd rasa`

run the server
`rasa run --enable-api`
