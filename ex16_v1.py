from sys import argv
script, filename = argv

#buka file, trus lihat isinya, trus tutup.
datanya = open(filename)
print(datanya.read())
datanya.close()

#buka file, trus edit isinya, save.
datanya = open(filename, "w")
isi = input("Masukkan kontennya: ")
datanya.write(isi)
datanya.close()
