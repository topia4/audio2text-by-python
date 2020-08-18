import speech_recognition as sp 

speak = sp.Recognizer()

with sp.AudioFile('xia-10.wav') as source:
    audio = speak.record(source)


try:
    print(speak.recognize_google(audio))
except sp.UnknownValueError:
    print('未能识别内容')
except sp.RequestError as er:
    print('网络错误')