from sys import argv

script, filename1 = argv

#pertama: nama file diinput waktu lagi unpack script
text1 = open(filename1)
print(f"Here's your file {filename1}:")
print(text1.read())

#kedua: nama file diinput setelah script dijalankan
print("Type the filename again:")
filename2 = input("> ")

text2 = open(filename2)
print(f"Here's your file {filename2}:")
print(text2.read())
