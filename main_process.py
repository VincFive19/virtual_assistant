# Imports
import openai
import requests
import os
from dotenv import load_dotenv

load_dotenv()



# Main Process

# Function: Generate audio stream and play on Raspberry Pi Speakers
# Input: text to be read by the voice
# Output: none
def generate_audio_stream(text):
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/" + os.getenv('VOICE_ID') + "/stream"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": os.getenv('ELEVENLABS_API_KEY')
    }

    data = {
        "text": "Some very long text to be read by the voice",
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0
        }
    }

    response = requests.post(url, json=data, headers=headers, stream=True)

    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)



# Function: Use Whisper to transcribe audio file
# Input: audio file
# Output: text
def whisper_transcribe(audio_file): 
    openai.api_key = os.getenv('OPENAI_API_KEY')
    audio_file = open("/path/to/file/audio.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)


#  Function: User GPT-4 ChatCompletion
#  Input: text
#  Output: text
def gpt4_chat_completion(text):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Completion.create(
        engine="davinci",
        prompt="This is a test",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n", " Human:", " AI:"]
    )
    print(response.choices[0].text)

    