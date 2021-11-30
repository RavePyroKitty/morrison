#import Utilities
import speech_recognition as sr

r = sr.Recognizer()

# Get the defult micerphone
with sr.Microphone() as source:
    # Listens to a command, using AVD (Automatic Device Setection)
    while True:
        audio = r.listen(source)

        # Recognizes speech using Google as a service: Online
        google = r.recognize_google(audio)
        sphinx = r.recognize_sphinx(audio)

        print("Google: \n" + google + "\n")
        print("Sphinx: \n" + sphinx + "\n")
