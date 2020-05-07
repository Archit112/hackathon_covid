from gtts import gTTS
import os

myText = "Text to speech conversion Using Python"

language = 'en'

output = gTTS(text = myText, lang = language, slow = False)

output.save("output_text_to_speech.mp3")

os.system("start output_text_to_speech.mp3")