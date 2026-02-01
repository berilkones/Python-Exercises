import random
import time

def zar_atma():
    return random.randint(1,6)



class Oyuncu:
    def __init__(self,isim):
        self.isim = isim
        self.puanlar = []
    def zar_at(self):
        sonuc = zar_atma()
        print(f"{self.isim} zar atti. Sonuc : {sonuc}\n")
        self.puanlar.append(sonuc)
        return sonuc
    def toplam_puan(self):
        return sum(self.puanlar)
    
def oyun():
    oyuncu1 = Oyuncu("beril")
    oyuncu2 = Oyuncu("beren")


    print("OYUN BASLIYOR!\n")
    i = 1

    while oyuncu1.toplam_puan() < 30 and oyuncu2.toplam_puan() < 30:

        print(f"{i}. tur!")

        oyuncu1.zar_at()
        time.sleep(2)
        oyuncu2.zar_at()
        time.sleep(2)

        i += 1





    print("OYUN BITTI!\n")

    print(f"{oyuncu1.isim} puani: {oyuncu1.toplam_puan()}\n")
    print(f"{oyuncu2.isim} puani: {oyuncu2.toplam_puan()}\n")

    if oyuncu1.toplam_puan() > oyuncu2.toplam_puan():
        print(f"{oyuncu1.isim} kazandi!")
    
    elif oyuncu2.toplam_puan() > oyuncu1.toplam_puan():
        print(f"{oyuncu2.isim} kazandi!")

    else:
        print("BERABERE!")



oyun()
