# LATIHAN
# Kalkulator sederhana 

print(20*"=")
print("kalkulator sederhana")
print(20*"=" + "\n")
angka_1 = float(input("masukan angka 1 = "))
operator = input("operator (+,-,*,/) : ")
angka_2 = float(input("masukan angka 2 = "))

# percabangan
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print("masukan yang bener dong, aku pusing")
print("Akhir dari program, terima kasih")