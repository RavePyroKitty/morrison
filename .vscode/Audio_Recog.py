
#import Utilities
import speech_recognition as sr

r = sr.Recognizer()

# Get the defult micerphone
with sr.Microphone() as source:
    # Listens to a command, using AVU
    audio = r.listen(source)

    text = r.recognize_google(audio)

    print(text)