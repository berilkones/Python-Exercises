import random 

def sayi_bulma():
    sayi = random.randint(1,100)
    skor = 100
    tahmin_sayisi = 0
    tahmin = int(input("Tuttuğum sayiyi tahmin edebilir misin\n"))

    while tahmin != sayi:
            
            if tahmin_sayisi == 10:
                break
            
            
            if tahmin < sayi:
               tahmin_sayisi += 1
               tahmin = int(input("Yanlis tahmin, daha buyuk bir tahminde bulun!\n"))

            elif tahmin > sayi:
               tahmin_sayisi += 1
               tahmin = int(input("Yanlis tahmin, daha kucuk bir tahminde bulun!\n"))

    
    if tahmin_sayisi == 10:
        print("Hakkiniz kalmamistir.\n")

    if tahmin == sayi:
       tahmin_sayisi += 1     
       print(f"Tebrikler,{tahmin_sayisi}. tahminde sonucu buldun!\n")
       print(f"skor:{skor - (tahmin_sayisi -1)*10}\n")

sayi_bulma()
    

