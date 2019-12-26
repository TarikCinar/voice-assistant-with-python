from bs4 import BeautifulSoup as bs
import urllib.request as istek

def cek():
    url = "https://www.msn.com/tr-tr/havadurumu/bugun/Ke%C5%9Fan,Edirne,T%C3%BCrkiye/we-city?iso=TR&el=ylemGn2jPiWeuoh5laVqSA%3D%3D"
    urlOku = istek.urlopen(url)
    veri = bs(urlOku, 'html.parser')
    sicaklik = veri.find_all('div', attrs={'class': 'current-info'})
    durum = veri.find_all('div', attrs={'class': 'weather-info'})
    sicak = sicaklik[0].text
    sicak = sicak[:4]
    dur = durum[0].text
    sayac=0
    for i in dur[:10]:
        if i!='':
            sayac+=1
    dur=dur[:10+sayac]

    gonder=("bugün hava"+dur+"sıcaklık "+sicak)
    return gonder

cek()


