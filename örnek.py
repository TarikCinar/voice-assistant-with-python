import random


class Dusman(object):
    def __init__(self, isim, can, mermi, saldırı_gucu):
        self.isim = isim
        self.can = can
        self.mermi = mermi
        self.saldırı_gucu = saldırı_gucu

    def yaz(self):
        print("--------------------------------------\n")
        print("isim=" + self.isim, "can=" + str(self.can), "mermi=" + str(self.mermi),
              "saldırı gucu=" + str(saldırı_gucu), sep="  ")
        print("--------------------------------------\n")

    def dusman_saldır(self):
        print("{}=saldırıyorummmm".format(self.isim))
        harcanan_mermi = random.randint(1, self.mermi)
        self.mermi-=harcanan_mermi
        print("harvanan mermi={}".format(mermi))
        return (harcanan_mermi* self.saldırı_gucu)

    def saldırıya_ugra(self, giden_can):
        print("{}=saldırıya ugradım".format(self.isim))
        self.can -= giden_can

    def mermi_bittimi(self):
        if mermi <= 0:
            print("mermi bitti")
        else:
            print(str(mermi) + " mermim kaldı")

    def hayattamı(self):
        if can <= 0:
            print("öldün")
        else:
            print(str(can) + " canım kaldı")


düşmanlar = []
for i in range(0, 5):
    can = random.randrange(100,200)
    mermi = random.randrange(10, 20)
    saldırı_gucu = random.randrange(10, 20)
    yeni_dusman = Dusman("dusman" + str(i + 1), can, mermi, saldırı_gucu)
    düşmanlar.append(yeni_dusman)

for i in range(5):
    saldıran = random.randrange(5)
    sadırıya_ugrayan = random.randrange(5)
    if saldıran == sadırıya_ugrayan:
        continue
    else:
        saldır = düşmanlar[saldıran].dusman_saldır()
        düşmanlar[saldıran].mermi_bittimi()
        düşmanlar[sadırıya_ugrayan].saldırıya_ugra(10)
        düşmanlar[sadırıya_ugrayan].hayattamı()