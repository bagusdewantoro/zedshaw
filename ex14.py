from sys import argv

kode, nama_user = argv
#contoh input = python ex14.py bagus
tanda = "--->>"

print(f"Hai {nama_user}, Saya adalah {kode} script.")
print("Saya mau tanya beberapa pertanyaan.")
print(f"Apakah kamu suka saya, {nama_user}?")
likes = input(tanda)

print(f"Where do you live {nama_user}?")
lives = input(tanda)

print("What kind of computer do you have?")
computer = input(tanda)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
