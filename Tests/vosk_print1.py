# Import libraries
from vosk import Model, KaldiRecognizer
import os
import pyaudio

def morrison():
    model = Model("model")
    rec = KaldiRecognizer(model, 1000)

# Opens microphone for listening
    p = pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=5000)
    stream.start_stream()

    while True:
        data = stream.read(4000)
        if len(data) == 9:
            break
        if rec.AcceptWaveform(data):
            print(rec.Result())
        else:
            print(rec.PartialResult())

    print(rec.FinalResult())

morrison()