from sys import exit

def ruang_emas():
    print("Ruang ini penuh emas. Berapa banyak yang kamu ambil?")
    choice = input ("> ")

    if choice.isnumeric():
        berapa = int(choice)
    else:
        dead("Belajar ketik angka dongg....")

    if berapa < 50:
        print("Bagus, kamu nggak pelit, kamu menang!")
        exit(0)
    else:
        dead("Maruk yaa!")

def ruang_beruang():
    print("Ada beruang disana.")
    print("Beruangnya punya madu yang sangat banyak.")
    print("Beruang yang gemuk ada di depan pintu satunya.")
    print("Bagaimana memindahkan beruang itu, 'ambil' madunya atau 'takutin' beruangnya?")
    beruang_gerak = False

    while True:
        choice = input("> ")

        if choice == "ambil":
            dead("Beruangnya nyerang, ")
        elif choice == "takutin" and not beruang_gerak:
            print("Beruangnya pindah dari pintu itu")
            print("Kamu bisa lewat pintu itu, mau 'takutin' beruangnya atau 'buka' pintunya?")
            beruang_gerak = True
        elif choice == "takutin" and beruang_gerak:
            dead("Beruangnya kaget dan menerkam kita")
        elif choice == "buka" and beruang_gerak:
            ruang_emas()
        else:
            print("Ketik yang benar sesuai pilihan yang ada..")

def ruang_monster():
    print("Disini kamu melihat monster besar")
    print("Apakah kamu akan 'lari' atau biarkan dia 'makan' kamu?")
    choice = input("> ")

    if "lari" in choice:
        mulai()
    elif "makan" in choice:
        dead("Dan beruang pun berkata \"Hmmm,,, enakk\"")
    else:
        ruang_monster()

def dead(kenapa):
    print(kenapa, "mantab!!")
    exit(0)

def mulai():
    print("Kamu ada di ruang gelap.")
    print("Ada pintu di sebelah 'kanan' dan 'kiri'mu.")
    print("Pintu mana yang akan kamu buka?")
    choice = input("> ")

    if choice == "kiri":
        ruang_beruang()
    elif choice == "kanan":
        ruang_monster()
    else:
        dead("Kamu bimbang sampai mati kelaparan.")

mulai()
