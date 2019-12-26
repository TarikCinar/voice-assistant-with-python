from bs4 import BeautifulSoup as bs
import urllib.request as istek

def kur_cek():
    url = "https://www.doviz.com/"
    urlOku = istek.urlopen(url)
    veri = bs(urlOku, 'html.parser')
    deger=veri.find_all('span',attrs={'class':'value'})
    altın=deger[0].text
    altın=altın[:5]
    dolar=deger[1].text
    dolar=dolar[:4]
    euro=deger[2].text
    euro=euro[:4]
    return ("altın "+altın+" dolar "+dolar+" euro "+euro)


kur_cek()


