from gtts import gTTS
from io import BytesIO
from playsound import playsound

def play(text):
    mp3_fp = BytesIO()
    tts = gTTS(text, 'en')
    tts.save('audio.mp3')
    playsound("audio.mp3")
