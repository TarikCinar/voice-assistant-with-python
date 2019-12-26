
sayılar=[] # boş bir dizi oluşturdum

kac_sayi_girilecek=int(input("kaç sayı girilecek: "))#kaç tane sayı girecek kullanıcı onu aldım

for i in range(kac_sayi_girilecek):#girilecek sayı kadar döngüyü dönderdim
    alınan_sayı=int(input(str(i)+".sayıyı girin: "))#her adımda bir sayı aldım
    sayılar.append(alınan_sayı)#ve aldıgım her sayıyı diziye attım artık alınan tüm sayılar bu dizi içerisinde

for i in range(kac_sayi_girilecek):
    print(sayılar[i])#girilen tüm sayıları listeledik



