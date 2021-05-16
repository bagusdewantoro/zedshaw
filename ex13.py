from sys import argv
s, a, b, c, d = argv #untuk c & d masukkan angka.
#(contoh ketik) python ex13.py bebas1 bebas2 4 7

a = input("Masukkan nama anak:")
b = input("Masukkan nama istri:")
x = float(c)
y = float(d)
e = (x*y)

print("The script is called:", s)
print("Your first variable is (nama anak):", a)
print("Your second variable is (nama istri):", b)
print("Your third variable is:", c)
print("Your fourth variable is:", d)

input("Bebas ketik apa aja:")
f = float(input("Masukkan angka pembagi:"))
g = (e/f)

print(f"{x} * {y} = ", e)
print(f"{e} / {f} = ", g)
print(f"Kamu bapak dari {a}, dan suami dari {b}.")
