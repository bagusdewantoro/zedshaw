import sys
script, kode, salah = sys.argv


def fungsi_utama(daftar_bahasanya, kode, ngaco):
    garis = daftar_bahasanya.readline()

    if garis:
        cetakgaris(garis, kode, ngaco)
        return fungsi_utama(daftar_bahasanya, kode, ngaco)


def cetakgaris(garis, kode, ngaco):
    baris_berikutnya = garis.strip()
    aslinya = baris_berikutnya.encode(kode, errors=ngaco)
    hasilnya = aslinya.decode(kode, errors=ngaco)

    print(aslinya, "<===>", hasilnya)


languages = open("languages.txt", encoding = "utf-8")

fungsi_utama(languages, kode, salah)
