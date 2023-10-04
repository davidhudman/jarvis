# Usage: python app.py "What is the OpenAI mission?"

import openai
import sys
import os
from gtts import gTTS

# read input from the cli python
input = sys.argv[1]
print(input)

# set the openai api key
openai.api_key = os.getenv('OPENAI_API_KEY')


completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": input}]
)

# print the message from the completion object
message = completion['choices'][0]['message']['content']
print(message)
tts = gTTS(message)
tts.save("openai.mp3")