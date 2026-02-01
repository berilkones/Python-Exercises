def palindrom(veri):
    dizi = []
    veri = veri.lower()
    veri = veri.strip()

    for i in range(len(veri)):
        dizi.append(veri[i])

    ters = dizi[::-1]

    if ters == dizi:
        print(f"{veri} bir palindromdur\n")

    else:
        print(f"{veri} bir palindrom değildir.\n")

    


veri = "ey Edip adanada pide ye"
palindrom(veri)


