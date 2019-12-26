import speech_recognition as sr
import os
from speech_recognition import Microphone
from hava_durumu import cek
from kur import kur_cek
from ceviri import cevir
from playsound import playsound
from gtts import gTTS
import time
import random



def dinle(data):
    
   
    def speak(audioString, dil):
        rnd=random.randint(1,1000)
        tts = gTTS(text=audioString, lang=dil)
        tts.save("audio{}.mp3".format(rnd))
        playsound('audio{}.mp3'.format(rnd))
        os.remove("audio{}.mp3".format(rnd))
    r = sr.Recognizer()
    data = data

    def dinle():
        with sr.Microphone() as source:
            print("bişeyler söyle")
            audio = r.listen(source)
        try:
            data = r.recognize_google(audio, language='tr-tr')
            data = data.lower()
            print("bunu söyledin :" + data)
            return data
        except sr.UnknownValueError:
            speak("ne söyledigini anlayamadım", "tr")

    # data = dinle()

    if "işletim sistemim" in data:
        sistem = os.name
        if sistem == "nt":
            #speak("işletim sisteminiz Windows", "tr")
            return "işletim sisteminiz Windows"

        else:
            speak("işletim sisteminiz linux", "tr")

    dizi = ["nasılsın", "ne yapıyorsun"]
    if data in dizi:
        speak("iyim teşekkür ederim", "tr")

    if "you tubeyi aç" == data:
        speak("you tubeyi açıyorum", "tr")
        os.startfile("https://www.youtube.com/?hl=tr&gl=TR")

    if "e-posta yolla" in data:
        from mail_gonderme import mailGonder
        speak("e posta alıcısı kim","tr")
        alınan=dinle()
        sozcuk={"tarık":"ersintarik89@gmail.com","betül":"betul.yeni@outloock.com"}
        if alınan in sozcuk.keys():
            speak("e postanın başlıgı ne olucak", "tr")
            baslık = dinle()
            speak("konusu içeriğini söyle", "tr")
            icerik = dinle()
            mailGonder(baslık, icerik,sozcuk[alınan])

    if "hava nasıl" in data:
        speak(cek(), "tr")
    dizi2 = ["döviz", "kur","ne kadar"]
    if data in dizi2:
        speak(kur_cek(), "tr")
    dizi3=["çeviri", "çevir"]
    if data in dizi3:
        speak("çevirmek istediğiniz cümleyi söyleyin", "tr")
        data = dinle()
        speak("hangi dile çeviri yapacaksınız", "tr")
        dil = dinle()
        veri = cevir(data, dil)
        speak(veri[0], veri[1])
    else:
        return "dediğini anlamadım"
data=""
calis(data)