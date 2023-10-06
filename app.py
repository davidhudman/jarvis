# Usage: python app.py "What is the OpenAI mission?"

import openai
import sys
import os
from gtts import gTTS

from record import createWav

# set the openai api key
openai.api_key = os.getenv('OPENAI_API_KEY')

createWav()

file = open("speech.wav", "rb")
transcription = openai.Audio.transcribe("whisper-1", file)
transcription = transcription['text']
print(transcription)


completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Write a 30 word response to the following question: " + transcription }]
)

# print the message from the completion object
message = completion['choices'][0]['message']['content']
print(message)
tts = gTTS(message)
tts.save("openai.mp3")

# play sound
file = "openai.mp3"
print('playing sound using native player')
os.system("afplay " + file + " -r 1.8")

# delete the file
os.remove(file)