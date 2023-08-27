import speech_recognition as sr
import pyttsx3 as pyt
import openai

r = sr.Recognizer()

#chatGPT setup
openai.api_key = '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'
messages = [{"role":"system","conext":"You are a snarky intelligent assistant"}]

def speak_text(message):
    engine = pyt.init()
    engine.say(message)
    engine.runAndWait()
    
recorded_message="An unknown error occured"
while(True):
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,0.2)
            
            audio = r.listen(source)
            
            recorded_message = r.recognize_google(audio)
            recorded_message = recorded_message.lower()
            
            #print("Did you say: ", recorded_message)
            speak_text(recorded_message)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occured")
        
    if(recorded_message):
        print("here")
        messages.append({"role":"user","content":"message"})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
        reply = chat.choices[0].message.content
        speak_text(reply)
