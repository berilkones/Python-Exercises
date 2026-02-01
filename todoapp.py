import json

DOSYA_ADI = "todo.json"

def dosya_yukle():
    try:
        with open(DOSYA_ADI, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def dosyayi_kaydet(veri):
    with open(DOSYA_ADI, "w") as file:
        json.dump(veri, file, indent = 4)


from datetime import datetime


def gorev_ekle():
    print("Yeni görev\n")
    baslik = input("Gorev basligi: \n")
    aciklama = input("Gorev aciklamasi: \n")
    tarih = input("Son tarih: \n")

    try:
        datetime.strptime(tarih, "%d/%m/%Y")
    except ValueError:
        print("Gecersiz tarih formati. Lutfen GG/MM/YY seklinde giriniz.")

        return 
    
    yeni_gorev = {
        "baslik" : baslik,
        "aciklama" : aciklama,
        "tarih" : tarih, 
        "tamamlandi" : False 
    }
    
    veri = dosya_yukle()
    veri.append(yeni_gorev)
    dosyayi_kaydet(veri)

    print("Gorev basariyla eklendi!\n")


def gorevleri_listele():
    veri = dosya_yukle()

    if not veri:
        print("Gorev bulunmamaktadir.\n")
        return
    
    print("Gorev listesi: \n")
    for i, gorev in enumerate(veri, start=1):
        durum = "✔" if gorev.get("tamamlandi", False) else "❌"
        print(f"{i}. [{durum}]{gorev['baslik']} - {gorev['tarih']}\n")
        print(f"  Aciklama: {gorev['aciklama']}\n")


def gorev_tamamla():
    veri = dosya_yukle()
    if not veri:
        print("gorev bulunmamakta\n")
        return
    print("Tamamlanacak görevler:\n")
    for i, gorev in enumerate(veri, start=1):
        durum = "✔" if gorev.get("tamamlandi", False) else "❌"
        print(f"{i}. [{durum}] {gorev['baslik']} - {gorev['tarih']}")

    try:
        secim = int(input("Tamamlanan gorevin numarasini girin.\n"))
        if secim < 1 or secim > len(veri):
            print("Gecersiz tercih!\n")
            return
        if veri[secim - 1]["tamamlandi"]:
            print("Bu görev zaten tamamlanmış.")
        else:
            veri[secim - 1]["tamamlandi"] = True
            dosyayi_kaydet(veri)
            print("Görev tamamlandı olarak işaretlendi! ✔️")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

    
    
    
    

