from sys import argv
script, filemasuk = argv

def printsemua(f):
    print(f.read())

def ulang(f):
    f.seek(0)

def print1baris(hitung, f):
    print(hitung, f.readline())

filebaru = open(filemasuk)

print("\nMari cetak seluruh baris: \n")
printsemua(filebaru)
input("\n(ketik 1 karakter apa aja untuk melanjutkan)\n")

print("Sekarang mari ulang, seperti cassette tape.")
ulang(filebaru)

print("Mari cetak 3 baris:\n")

garisbaru = 1
print1baris(garisbaru, filebaru)

garisbaru += 1
print1baris(garisbaru, filebaru)

garisbaru += 1
print1baris(garisbaru, filebaru)

#ini manual tanpa def
garisbaru += 1
print(garisbaru, filebaru.readline())
