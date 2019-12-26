import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

def mailGonder(baslık ,icerik,alıcı):
    message = MIMEMultipart()

    message["From"] = "ersintarik89@gmail"+".com"  # Mail'i gönderen kişi

    message["To"] = alıcı # Mail'i alan kişi

    message["Subject"] = baslık  # Mail'in konusu

    body = icerik  # Mail içerisinde yazacak içerik

    body_text = MIMEText(body, "plain")  #

    message.attach(body_text)

    # Gmail serverlerine bağlanma işlemi.
    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)

        mail.ehlo()

        mail.starttls()

        mail.login("ersintarik89@gmail.com", "ZAkmn2375.")

        mail.sendmail(message["From"], message["To"], message.as_string())

        #print("Mail Başarılı bir şekilde gönderildi.")

        mail.close()
    # Eğer mesaj gönderirken hata ile karşılaşırsak except çalışır.
    except:
        sys.stderr.write("Bir hata oluştu. Tekrar deneyin...")
        sys.stderr.flush()
