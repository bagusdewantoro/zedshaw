print("Ini \'escape kutip, \\ escape , \ tes")
print("\n garis baru dan \t tabs")

puisi = """
\tPuisi apa aja
Cuman buat ngetes
Ini garis baru \n bener ngga
coba aja
\n\t garis baru dan tab
"""

print(puisi, "\n")

def rumus(a):
    buncis = a * 500
    kendi = buncis / 1000
    pak = kendi / 100
    return buncis, kendi, pak

awal = 10000
print(rumus(awal))
bolu, brownies, lontong = rumus(awal)

print("Nilai awal adalah: {}".format(awal))
print(f"Kita punya {bolu} bolu, {brownies} brownies, {lontong} lontong")

awal = awal/10
rumus_baru = rumus(awal)
print("kita punya {} bolu, {} brownies, {} lontong".format(*rumus_baru))
