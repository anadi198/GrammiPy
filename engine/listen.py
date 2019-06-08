import speech_recognition as sr
import api2
import tts

sample_rate = 48000  #how often values are recorded
chunk_size = 2048   #buffer
r = sr.Recognizer()

with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print("Say something")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        t = list(text)
        t[0] = t[0].capitalize()
        text = ''.join(t)    
        print("you said: " + text)
        response = api2.checkGrammar(text)
        print(response)
        tts.play(response)

    except sr.UknownValueError:
        print("Google Speech Recognition could not understand the audio.")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))             

