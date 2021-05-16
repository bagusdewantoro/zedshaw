hitung = [1, 2, 3, 4, 5]
buah = ["apel", "jeruk", "pir", "alpukat"]
uang = [1, "kertas", 2, "logam", 3, "cek"]

for angka in hitung:
    print(f"Ini adalah angka {angka}")
print("__________________________", "\n")

for jenis in buah:
    print(f"Ini adalah buah {jenis}")
    uang.append(jenis)
print("__________________________", "\n")

for i in uang:
    print(f"Saya punya {i}")
print("__________________________", "\n")


elemen = []

for i in range (0, 6):
    print(f"Tambahkan {i} pada list.")
    elemen.append(i)
print("__________________________", "\n")

for i in elemen:
    print(f"elemen adalah: {i}")
