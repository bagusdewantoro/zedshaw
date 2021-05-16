def urutan(i,x, tingkat):
    numbers = []
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)
        print(f"Numbers now: {numbers}")
        i += tingkat
        print(f"At the bottom i is {i}")
    print("The numbers:")
    for num in numbers:
        print(num)

x = int(input("Masukkan x: "))
y = int(input("Masukkan y: "))
z = int(input("Masukkan tingkat: "))
urutan(x,y,z)
