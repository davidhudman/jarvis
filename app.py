import openai
from gtts import gTTS
tts = gTTS('hello my name is susan')
tts.save('hello.mp3')


# completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "What is the OpenAI mission?"}]
# )
completion = {
    "id": "chatcmpl-860ICXhpI2RDn6yFcubZQpohyDvky",
    "object": "chat.completion",
    "created": 1696441784,
    "model": "gpt-3.5-turbo-0613",
    "choices": [
        {
          "index": 0,
          "message": {
              "role": "assistant",
              "content": "The OpenAI mission is to ensure that artificial general intelligence (AGI) benefits all of humanity. AGI refers to highly autonomous systems that outperform humans at most economically valuable work. OpenAI aims to build safe and beneficial AGI directly, but if another project comes close to building AGI before they do, they commit to stop competing and start assisting that project instead. Their primary focus is to ensure that AGI development is carried out in a safe, responsible, and cooperative manner to avoid harmful effects and maximize societal benefits."
          },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 14,
        "completion_tokens": 106,
        "total_tokens": 120
    }
}

print(completion)
