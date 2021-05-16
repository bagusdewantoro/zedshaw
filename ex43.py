from sys import exit
from random import randint
from textwrap import dedent


class Adegan(object):
    def masuk(self):
        print("Adegan ini belum di-set")
        print("Subclass it and implement enter().")
        exit(1)


class Mesin(object):
    def __init__(self, peta_adegan):
        self.peta_adegan = peta_adegan
    def main(self):
        adegan_sekarang = self.peta_adegan.adegan_pembuka()
        adegan_terakhir = self.peta_adegan.adegan_next('selesai')
        while adegan_sekarang != adegan_terakhir:
            nama_adegan_next = adegan_sekarang.masuk()
            adegan_sekarang = self.peta_adegan.adegan_next(nama_adegan_next)
        #Pastikan untuk print out adegan terakhir:
        adegan_sekarang.masuk()


class Kalah(Adegan):
    ejekan = [
        "Kamu mati.., bener-bener payah",
        "Seandainya kamu lebih pintar..",
        "Pecundang..",
        "Bahkan anjing kecil saya lebih pintar.."
        "Kalah totalll"
    ]
    def masuk(self):
        print(Kalah.ejekan[randint(0, len(self.ejekan)-1)])
        exit(1)


class KoridorUtama(Adegan):
    def masuk(self):
        print(dedent("""
            Gothon dari Planet Percal menyerang dan
            menghancurkan pasukanmu. Kamu adalah anggota
            terakhir dan misimu adalah mendapat bom nuklir
            dari persenjataan, dan hancurkan kapalnya
            setelah berhasil kabur.

            Kamu lari di koridor utama menuju gudang
            persenjataan ketika Gothon datang. Dia
            menghalangi pintu persenjataan dan hampir
            menembakmu."""))

        aksi = input("> ('tembak', 'hindari', 'bercanda'): ")

        if aksi == "tembak":
            print(dedent("""
                Dengan cepat kostumnya hancur, dia sangat
                marah dan langsung menembakmu berkali-kali.
                Kemudian dia memakanmu."""))
            return 'mati'
        elif aksi == "hindari":
            print(dedent("""
                Kamu menghindar dengan tangkas, tapi malah
                terpeleset, dia dengan cepat menginjak dan
                memakanmu."""))
            return 'mati'
        elif aksi == "bercanda":
            print(dedent("""
                Beruntung, dia suka bercanda, lalu dia ketawa,
                dan kemudian kamu bisa tembak dia, lalu langsung
                menuju pintu gudang senjata."""))
            return 'gudang_senjata'
        else:
            print("Salah Ngetik!")
            return 'koridor_utama'


class SenjataLaser(Adegan):
    def masuk(self):
        print(dedent("""
            Kamu masuk gudang senjata, ngecek barangkali ada
            Gothon lain. Kamu menemukan bom neutron. Perlu
            memasukkan kode max 10 kali, kodenya 3 digit,
            jika salah, bomnya failed selamanya"""))

        kode = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        tebak = int(input("[keypad]> "))
        tebakan = 0

        while tebak != kode and tebakan < 10:
            # DUA BARIS DI BAWAH INI ADALAH CHEAT TAMBAHAN DARI BAGUS:
            if tebak == 777:
                return 'jembatan'
            # DI BAWAH INI SUDAH SESUAI ASLINYA:
            print("BZZZZDDD")
            tebakan += 1
            tebak = int(input("[keypad]> "))

        if tebak == kode:
            print(dedent("""
                Kotaknya terbuka, kamu ambil bom, lari
                secepat mungkin ke jembatan dan harus
                meletakkan di tempat yang tepat."""))
            return 'jembatan'

        else:
            print(dedent("""
                Kotaknya terkunci, kamu cuman bisa terdiam.
                Gothon meledakkan kapa dan kamu mati."""))
            return 'mati'


class Jembatan(Adegan):
    def masuk(self):
        print(dedent("""
            Kamu lari menuju jembatan membawa bom neutron
            dan hendak menaruhnya di sana dengan tepat.
            5 Gothon kaget dan mereka ngga mau menembakmu
            karena kamu bawa bom itu."""))

        aksi = input("> ('buru-buru taruh', 'taruh perlahan') : ")

        if aksi == "buru-buru taruh":
            print(dedent("""
                Kamu tidak menaruh di tempat yang tepat.
                Bom gagal meledak, lalu Gothon menembakmu."""))
            return 'mati'
        elif aksi == "taruh perlahan":
            print(dedent("""
                Bom terpasang dengan benar. Para Gothon takut.
                Kamu berlari menuju pintu dan menguncinya. Lalu
                kamu lari ke tempat melarikan diri."""))
            return 'alat_kabur'
        else:
            print("SALAH KETIK!")
            return 'jembatan'


class Alat_Kabur(Adegan):
    def masuk(self):
        print(dedent("""
            Kamu buru-buru masuk ke kapal mencoba kabur dengan alat
            untuk melarikan diri. Ada 5 alat, pilih yang mana?"""))

        alat_bener = randint(1,5)
        tebak = input("[alat #]> ")

        if int(tebak) == 777:
            print(dedent("""
                Kamu berhasil kabur dan para Gothon meledakk!!!"""))
            return 'tamat'
        elif int(tebak) != alat_bener:
            print(dedent(f"""
                Kamu pilih alat nomor {tebak} dan mengancurkan
                seluruh kapal."""))
            return 'mati'
        elif int(tebak) == alat_bener:
            print(dedent("""
                Kamu berhasil kabur dan para Gothon meledakk!!!"""))
            return 'tamat'


class Tamat(Adegan):
    def masuk(self):
        print("Kamu menang! Selamat!")
        # return 'tamat'    ##--> Ini kode asli ZED
        # DI BAWAH INI MODIFIKASI BAGUS:
        return exit(1)

class Peta(object):
    adegan_adegan = {
        'koridor_utama' : KoridorUtama(),
        'gudang_senjata' : SenjataLaser(),
        'jembatan' : Jembatan(),
        'alat_kabur' : Alat_Kabur(),
        'mati' : Kalah(),
        'tamat' : Tamat()
    }

    def __init__(self, adegan_awal):
        self.adegan_awal = adegan_awal
    def adegan_next(self, nama_adegan):
        val = Peta.adegan_adegan.get(nama_adegan)
        return val
    def adegan_pembuka(self):
        return self.adegan_next(self.adegan_awal)

a_map = Peta('koridor_utama')
a_game = Mesin(a_map)
a_game.main()
