from ArayuzKodları import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import speech_recognition as sr
from speech_recognition import Microphone
from hava_durumu import cek
from kur import kur_cek
from ceviri import cevir
from playsound import playsound
from gtts import gTTS
import random
from selenyum import ara
import sys
from keyboard import press
import time
from Firebase import olc
from help import *
from help_mesaj import mesaj
import os
from Eposta import *
from mail_gonderme import mailGonder




class deneme(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_widget()
        self.ui.setupUi(self)
        self.ui.gonder.clicked.connect(self.kullanici_yaz)
        self.ui.lineEdit.returnPressed.connect(self.ui.gonder.click)
        self.pen = QMainWindow()
        self.eposta = Ui_Form_E()
        self.eposta.setupUi_E(self.pen)
        self.eposta.gonder_button.clicked.connect(self.eposta_gonder)
        self.eposta.iptal_button.clicked.connect(self.eposta_iptal)


    def help(self):
        self.window=QMainWindow()
        self.help=Ui_Form()
        self.help.setupUi(self.window)
        self.help.textBrowser.append(mesaj())
        self.window.show()

    def kucult(self):
        self.showMinimized()

    def kullanici_yaz(self,deger=1):
        yazi=self.ui.lineEdit.text()
        yazi.lower()
        if len(yazi)<1:
            return
        self.ui.text_b.append("""<p align="left"><font face="consolas"  color="#DCDCDC">
                            <b>[SİZ] --{}</b></font></p>""".format(yazi))
        self.islem(yazi, 0)
        self.ui.lineEdit.clear()

    def asistan_yaz(self,data,deger=1):
        if deger:
            self.ui.text_b.append("""<p align=left><font face="consolas" size="3" color="#00FF7F">
                    <b>[ASİSTAN] --{}</b></font></p>""".format(data))
    def kapat(self):
        self.close()

    def eposta_gonder(self):
        self.kime=self.eposta.kimeLabel.text()
        self.baslik=self.eposta.baslikLabel.text()
        self.konu=self.eposta.konuLabel.toPlainText()
        print(self.baslik,self.kime,self.konu)
        if len(self.kime)<1:
            self.eposta.uyari.setText("Kime alanı boş geçilemez!!")
        else:
            mailGonder(self.baslik, self.konu, self.kime)
            self.pen.close()
            self.asistan_yaz("e-posta başarılı bir şekilde yollandı")
            self.eposta.konuLabel.clear()
            self.eposta.kimeLabel.clear()
            self.eposta.konuLabel.clear()


    def eposta_iptal(self):
        self.pen.close()
        self.asistan_yaz("e-posta gönderme işlemi iptal edildi")
    def islem(self,data,deger):
        if "sıcaklık" in data or "nem" in data:
            self.asistan_yaz(olc())
            self.speak(olc(),"tr",deger)
        elif "temizle" in data or "clear" in data:
            self.ui.text_b.clear()
        elif "mail" in data or "gmail" in data:
            self.asistan_yaz("Mail' ini açıyorum")
            self.speak("mail' ini açıyorum", "tr", deger)
            os.startfile("https://mail.google.com/mail/u/0/#inbox")

        elif "google" in data:
            index=data.index("google")
            yazi=data[:index]
            self.asistan_yaz("{} senin için google'da arıyorum".format(yazi))
            self.speak("{} senin için google'da arıyorum".format(yazi),"tr",deger)
            time.sleep(1)
            ara(yazi)

        elif "merhaba" in data or "merhabalar" in data or "selam" in data:
            self.asistan_yaz("Merhaba tarık")
            self.speak("merhaba tarık","tr",deger)
        elif "işletim sistemim" in data:
            sistem = os.name
            if sistem == "nt":
                self.speak("işletim sisteminiz Windows", "tr",deger)
                self.asistan_yaz("İşletim sisteminiz windows")
            else:
                self.speak("işletim sisteminiz linux", "tr",deger)
                self.asistan_yaz("İşletim sisteminiz linux")
        elif "klasörü oluştur" in data or "klasör oluştur" in data:
            data=data[:-15]
            try:
                os.mkdir("C:/Users/tarık çinar/Desktop/{}".format(data))

            except FileExistsError:
                self.asistan_yaz("Bu klasörden zaten var")
                self.speak("bu klasörden zaten var","tr",deger)
                return

            self.speak("{} adında bir klasör oluşturdum".format(data), "tr", deger)
            self.asistan_yaz("{} adında bir klasör oluşturdum".format(data))
        elif "nasılsın" in data:
            self.speak("iyim teşekkür ederim", "tr",deger)
            self.asistan_yaz("İyim teşekkür ederim")

        elif "YouTube" == data:
            self.speak("you tubeyi açıyorum", "tr",deger)
            self.asistan_yaz("YouTube'yi açıyorum")
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "https://www.youtube.com/?hl=tr&gl=TR"])

        elif "posta" in data:
            self.pen.show()

        elif "hava nasıl" in data:
            self.speak(cek(), "tr",deger)
            self.asistan_yaz(cek())


        elif "döviz" in data:
            self.speak(kur_cek(), "tr",deger)
            self.asistan_yaz(kur_cek())


        elif "çeviri" in data:
            self.speak("çevirmek istediğiniz cümleyi söyleyin", "tr",deger)
            self.asistan_yaz("Çevirmek istediğiniz cümleyi söyleyin")
            data = self.dinle(1)
            self.speak("hangi dile çeviri yapacaksınız", "tr",deger)
            self.asistan_yaz("Hangi dile çeviri yapacaksınız")
            dil = self.dinle(1)
            veri = cevir(data, dil)
            self.speak(veri[0], veri[1],deger)
            self.asistan_yaz(veri[0])
        else:
            self.asistan_yaz("{} ile ne demek istediğini anlamadım".format(data))
            self.speak( "{} ile ne demek istediğini anlamadım".format(data),"tr",deger)

    def ceviri(self):

        with sr.Microphone() as source:
            print("bişeyler söyle")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            data = r.recognize_google(audio, language='tr-tr')
            data = data.lower()
            print("bunu söyledin:"+data)
            return data
        except sr.UnknownValueError:
            self.speak("Ne söyledigini anlayamadım", "tr",1)
            self.asistan_yaz("Ne söylediğini anlamadım")
            print("Ne söylemek istediğini anlamadım")
    def speak(self,audioString,dil,deger):
        if deger:
            rnd = random.randint(1, 1000)
            tts = gTTS(text=audioString, lang=dil)
            tts.save("audio{}.mp3".format(rnd))
            playsound('audio{}.mp3'.format(rnd))
            os.remove("audio{}.mp3".format(rnd))

    def dinle(self,deger=0):
        r = sr.Recognizer()
        data = ""

        with sr.Microphone() as source:
            print("bişeyler söyle")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            data = r.recognize_google(audio,language='tr-tr')
            data = data.lower()
            print("bunu söyledin:" + data)
            if deger:
                return data
            else:
                self.islem(data, 1)
        except sr.UnknownValueError:
            self.speak("Ne söyledigini anlayamadım", "tr", 1)
            self.asistan_yaz("Ne söylediğini anlamadım")

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        # print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

uygulama=QApplication([])
pencere=deneme()
pencere.setWindowFlags(QtCore.Qt.FramelessWindowHint)
pencere.show()
uygulama.exec()



