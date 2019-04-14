import speech_recognition as sr
import ATD

sample_rate = 48000  #how often values are recorded
chunk_size = 2048    #buffer
r = sr.Recognizer()

with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print("Say something")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("you said: " + text)

    except sr.UknownValueError:
        print("Google Speech Recognition could not understand the audio.")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))   


ATD.setDefaultKey("018f415dc8592124d036b9857a35a9dd44")
#print(text)
errors = ATD.checkGrammar("text is eats")
#print(text)
for error in errors:
    print("hi")
    # print("%s error for: %s **%s**"%(error.type, error.precontext, error.string))
    #print("Some suggestions: %s"%(", ".join(error.suggestions),))            

