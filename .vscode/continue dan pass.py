## continue dan pass

# pass-> dia berfungsi sebagai dummy, tidak akan di eksekusi
angka = 0
while angka < 5:
    angka += 1

    if angka == 3:
        pass # ini tidak akan di eksekusi
    print(angka)

# continue

angka = 0
print(f"angka sekarang -> {angka}")
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1

    if angka ==3:
        print("nice!")
        continue # akan membuat loop meloncat ke awal
    print("whatsup")
print("finish")