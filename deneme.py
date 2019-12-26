from speech_recognition import *
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("bişeyler söyle")
    r.adjust_for_ambient_noise(source)

    audio = r.listen(source)
print("burdayım")
try:
    data = r.recognize_google(audio, language='tr-tr')
    data = data.lower()
    print("bunu söyledin:" + data)
except:
    print("aa")



