gen1 = {
    "Hera" : "Bagus",
    "Heru" : "Wisnu",
    "Ati" : "Theo"
}

gen2 = {"Bagus" : "Dhira", "Wisnu": "Uget", "Theo" : "Chelsea"}

print(f"Anaknya Hera adalah", gen1["Hera"])
print(f"Anaknya Wisnu adalah", gen2["Wisnu"])
print("\n")

for a, b in list(gen1.items()):
    print(f"{a} adalah orangtua dari {b}")

for a, b in list(gen1.items()):
    print(f"{a} adalah orangtua dari {b}", end= " ")
    print(f"dan grandparent dari {gen2[b]}")
