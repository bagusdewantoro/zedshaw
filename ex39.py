propinsi = {
    "Jakarta" : "JKT",
    "Jabar" : "JB",
    "Jatim" : "JT",
    "Banten" : "B",
    "Yogyakarta" : "YK"
}
print("\nBerikut 5 propinsi: \n", propinsi, "\n")

kota = {
    "JT" : "Surabaya",
    "YK" : "Sleman",
    "JB" : "Bandung"
}
print("Kota yang sudah diinput: \n", kota, "\n")

kota["B"] = "Serang"
kota["JKT"] = "Jakpus"
print("Update input kota: \n", kota, "\n")

print("-" * 10, "SINGKATAN")
print("Singkatan Yogyakarta adalah", propinsi["Yogyakarta"])
print("Singkatan Jabar adalah", propinsi["Jabar"], "\n")

print("-" * 10, "IBUKOTA")
print("Ibukota Yogyakarta adalah", kota[propinsi["Yogyakarta"]])
print("Ibukota Jabar adalah", kota[propinsi["Jabar"]], "\n")

print("-" * 10, "SINGKATAN SEMUANYA")
for prop2, singkatan in list(propinsi.items()):
    print(f"{prop2} disingkat sebagai {singkatan}")

print("\n", "-" * 10, "IBUKOTA SEMUANYA")
for singkatan, ibukota in list(kota.items()):
    print(f"{singkatan} punya kota {ibukota}")

print("\n", "-" * 10, "SINGKATAN & IBUKOTA")
for prop2, singkatan in list(propinsi.items()):
    print(f"{prop2} disigkat {singkatan}", end=" ")
    print(f"dan punya ibukota {kota[singkatan]}")

print("\n", "-" * 10)
prop2 = propinsi.get("Texas")

if not propinsi:
    print("Maaf, tidak ada Texas")

ibukota = kota.get("TX", "Tidak ada")
print(f"Ibukota untuk propinsi 'TX' : {ibukota}")
