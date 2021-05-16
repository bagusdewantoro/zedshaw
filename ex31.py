print("Ada dua pintu, pilih pintu #1 atau pintu #2?")
pintu = input("> ")

if pintu == "1":
    print("Ada beruang besar makan kue, lo mau ngapain?")
    print("1. Ambil kuenya")
    print("2. Teriakin beruangnya")
    cabang1 = input("> ")

    if cabang1 == "1":
        print("Beruangnya makan muka elo, hahaha")
    elif cabang1 == "2":
        print("Beruangnya makan kaki elo, hahaha")
    else:
        print("Ini adalah pilihan yang tepat")

elif pintu == "2":
    print("Lo melihat kebun buah-buahan")
    print("1. Pilih apel")
    print("2. Pilih jeruk")
    print("3. Pilih pisang")
    cabang2 = input("> ")

    if cabang2 == "1" or cabang2 == "2":
        print("Oke, cakep")
    elif cabang2 == "3":
        print("Pisangnya busuk")
    else:
        print("Ya udah ngga makan buah sama sekali")

else:
    print("Salah pilih, orang disuruhnya 1 dan 2")
