# Peta:
#   - Adegan berikutnya
#   - Adegan awal
# Mesin:
#   - main
# Adegan:
#   - masuk
#   - Kalah
#   - Koridor Utama
#   - Senjata Laser
#   - Jembatan
#   - Lolos

class Adegan(object):
    def masuk(self):
        pass

class Mesin(object):
    def __init__(self, peta_adegan):
        pass
    def main(self):
        pass

class Kalah(Adegan):
    def masuk(self):
        pass

class KoridorUtama(Adegan):
    def masuk(self):
        pass

class SenjataLaser(Adegan):
    def masuk(self):
        pass

class Jembatan(Adegan):
    def masuk(self):
        pass

class Peta(object):
    def __init__(self, mulai_adegan):
        pass
    def adegan_next(self, nama_adegan):
        pass
    def adegan_awal(self):
        pass

a_map = Peta('koridor_utama')
a_game = Mesin(a_map)
a_game.main()
