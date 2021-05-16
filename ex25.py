def pisah_kata(pernik):
    """Fungsi ini akan memecah kata"""
    kata = pernik.split(" ")
    return kata

def pilah_kata(kata):
    """Pilah kata"""
    return sorted(kata)

def cetak_kata_pertama(kata):
    """Cetak kata pertama setelah muncul"""
    kata2 = kata.pop(0)
    print(kata2)

def cetak_kata_terakhir(kata):
    """Cetak kata terakhir setelah muncul"""
    kata2 = kata.pop(-1)
    print(kata2)

def pilah_kalimat(kalimat):
    """Ambil satu kalimat dan jadikan pilah kata"""
    kata = pisah_kata(kalimat)
    return pilah_kata(kata)

def cetak_kata_pertama_dan_terakhir(kalimat):
    """Cetak kata pertama dan terakhir"""
    kata = pisah_kata(kalimat)
    cetak_kata_pertama(kata)
    cetak_kata_terakhir(kata)

def cetak_pilahan_pertama_dan_terakhir(kalimat):
    """Pilah kata lalu cetak yang pertama dan terakhir"""
    kata = pilah_kalimat(kalimat)
    cetak_kata_pertama(kata)
    cetak_kata_terakhir(kata)
