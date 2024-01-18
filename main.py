import os
from google.cloud import texttospeech_v1

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"
client = texttospeech_v1.TextToSpeechClient()

text = "../pdf/sample.pdf"

synthesis_input = texttospeech_v1.SynthesisInput(text=text)

voice = texttospeech_v1.VoiceSelectionParams(
    language_code= "en-in",
    ssml_gender= texttospeech_v1.SsmlVoiceGender.FEMALE ,
)

# print(dir(texttospeech_v1.SsmlVoiceGender))
# print(client.list_voices())

audio_config = texttospeech_v1.AudioConfig(
    audio_encoding= texttospeech_v1.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input,
    voice= voice,
    audio_config=audio_config
)

with open("output_audio.mp3", "wb") as file:
    file.write(response.audio_content)
    print("audio content created successfully")

