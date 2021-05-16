from sys import argv
from os.path import exists
script, datalama, databaru = argv

isi = open(datalama).read()

print("Berikut ini isinya : \n", isi)
print(f"Jumlah karakter = {len(isi)} bytes")
print(f"Apakah file baru sudah ada? {exists(databaru)}")

kontenbaru = open(databaru, "w")
kontenbaru.write(isi)
