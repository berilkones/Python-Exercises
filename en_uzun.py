def en_uzun_bul(cumle):
    
    dizi = cumle.split(" ")
    print(f"{dizi}")

    uzunluk = 0
    kelime = []
    

    for i in range(len(dizi)):

        if uzunluk == len(dizi[i]):
            kelime.append(dizi[i])

        elif len(dizi[i]) > uzunluk:
            uzunluk = len(dizi[i])
            kelime = [dizi[i]]
            
        else:
            continue
    print(f"cumlenin en uzun kelimesi: {kelime}\n")



en_uzun_bul("bazi konulari başarmak için hirsli olman lazim")