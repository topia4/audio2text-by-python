import speech_recognition as sr 
r = sr.Recognizer
with sr.AudioFile('u02t2.wav') as source:
    audio = r.record(source)
try:
        text = r.recognize_google(audio)
        print('working on...')
        print(text)
except:
        print('sorry.. run again...')