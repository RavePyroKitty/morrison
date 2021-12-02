#import Utilities
import speech_recognition as sr
import datetime

r = sr.Recognizer()

# Get the defult micerphone
with sr.Microphone() as source:
    # Listens to a command, using AVD (Automatic Device Setection)
    while True:
        audio = r.listen(source)

        # Recognizes speech using Google as a service: Online
        text = r.recognize_google(audio)

        print(text)
        #if str(text).lower() == "what time is":
        #    print(datetime.datetime.now().strftime())
        #    break