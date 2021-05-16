awal = "Apel Jeruk Burung Telepon Lampu Gula"
akhir = awal.split(" ")
tambahan = ["Siang", "Malam", "Lagu", "Bumerang", "Jagung", "Pisang", "Cewe", "Cowo"]
print("awal: ", awal)
print("tambahan: ", tambahan)

while len(akhir) != 10:
    berikutnya = tambahan.pop()
    print("Tambahkan: ", berikutnya)
    akhir.append(berikutnya)
    print(f"Sekarang jumlah barangnya ada: {len(akhir)} \n")

print("tambahan: ", tambahan)
print("pop tambahan: ", tambahan.pop())
print("sekarang list barangnya: ", akhir, "\n")

print(akhir[1])
print(akhir[-1])
print(akhir[-3], "\n")

print(akhir.pop(), "\n")

print(" ".join(akhir))
print("**".join(akhir[3:6]))
