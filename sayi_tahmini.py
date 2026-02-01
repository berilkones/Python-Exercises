import random

def sayi_tahmini():
    sayi = random.randint(1,100)

    deneme = 0

    tahmin = int(input("1 ile 100 arasinda bir sayi tuttum, tahmin et bakalim!\n"))

    while sayi != tahmin:

        if sayi < tahmin:
            deneme += 1
            tahmin=int(input("yanlis tahmin, daha küçük bir sayi dene\n"))
            

        elif sayi > tahmin:
            deneme += 1
            tahmin=int(input("yanlis tahmin, daha buyuk bir sayi dene\n"))
            
        
    if sayi == tahmin:
        deneme += 1
        print(f"tebrikler! doğru tahmini {deneme}. tahminde bildin\n")

    


    
sayi_tahmini()
    

