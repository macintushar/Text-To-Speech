from gtts import gTTS
from playsound import playsound
import os

def textToSound(txt):
    tts = gTTS(txt)
    tts.save('sound.mp3')
    playsound(r'sound.mp3')
    os.remove('sound.mp3')

inp = input('Enter the text to convert to speech: ')
textToSound(txt=inp)
