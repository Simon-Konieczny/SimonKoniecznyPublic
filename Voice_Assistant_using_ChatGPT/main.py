import speech_recognition as sr
import pyttsx3 as pyt

r = sr.Recognizer()

def speak_text(message):
    engine = pyt.init()
    engine.say(message)
    engine.runAndWait()
    

while(True):
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,0.2)
            
            audio = r.listen(source)
            
            recorded_message = r.recognize_google(audio)
            recorded_message = recorded_message.lower()
            
            print("Did you say: ", recorded_message)
            speak_text(recorded_message)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occured")
