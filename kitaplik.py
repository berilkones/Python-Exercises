kitaplar = []





def yeni_kitap_ekleme():
    isim = input("kitap ismi: ")
    yazar = input("kitabin yazari: ")
    yil = input("kitabin basim yili: ")

    yeni_kitap = {
        "isim": isim,
        "yazar" : yazar,
        "yil": yil
    }

    kitaplar.append(yeni_kitap)

def kitap_sil(isim, kitaplar):
    bulundu = False
    for kitap in kitaplar:
        if kitap["isim"] == isim:
            kitaplar.remove(kitap)
            print(f"{isim} adli kitap silindi.\n")
            bulundu = True
            break

    if not bulundu:
        print("kitap bulunamadi")


def listele(kitaplar):
    for kitap in kitaplar:
        print(f"{kitap}\n")


def kitap_ara(kitaplar, isim):
    bulundu = False
    for kitap in kitaplar:
        if kitap["isim"] == isim:
            print(f"kitap ismi : {isim}\n")
            print(f"kitap ayzari: {kitap['yazar']}\n")
            print(f"kitap yili : {kitap['yil']}\n")
            bulundu = True
            break
    if not bulundu:
        print("kitap bulunamadi\n")



print("yeni kitap eklemek icin: 1\n")
print("kitap silmek icin: 2\n")
print("kitaplari listelemek icin: 3\n")
print("kitap aramak icin: 4\n")
print("cikis yapmak icin: 5\n")

islem = int(input("lütfen bir islem seciniz: "))

while islem != 5:
    if islem == 1:
        yeni_kitap_ekleme()

    elif islem == 2:
        isim = input(("lutfen silmek istediginiz kitabin ismini giriniz.\n"))
        kitap_sil(isim,kitaplar)

    elif islem == 3:
        listele(kitaplar)

    elif islem == 4:
        isim = input(("lutfen aramak istediginiz kitabin ismini giriniz.\n"))
        kitap_ara(kitaplar,isim)

    elif islem == 5: 
        print("cikis yapiliyor...")
        break

    islem = int(input(
    "isleminizi seciniz.\n"
    "yeni kitap eklemek icin 1,"
    "kitap silmek icin 2,"
    "kitaplari listelemek icin 3,"
    "kitap aramak icin 4,"
    "cikis yapmak icin 5 tuslarina basiniz."
))


