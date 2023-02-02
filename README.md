# Robotics-Project-II-Midterm-Project

# Details

tts_url = 'http://localhost:5001/tts'
asr_url = 'http://localhost:5002/stt'
rasa_url = 'http://localhost:5005/model/parse'

## Run ASR

`cd asr`

`python asr.py`

## Run TTS

`cd tts`

`python tts.py`

## Run RASA

`cd rasa`

`rasa run --enable-api`

in a separate terminal
`rasa run actions`
