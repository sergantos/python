from gtts import gTTS
import os

text = 'Привет, любимый!'

tts = gTTS(text=text, lang='ru')
tts.save("1.mp3")

os.system("1.mp3")