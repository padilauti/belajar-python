# looping dari list

# for loop
print("For Loop")
kumpulan_angka = [4,2,3,5,6,1]
for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["uti","nur","padila","ilham","diah","april"]
for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print("\nFor Loop dan range")
kumpulan_angka = [10,5,4,2,6,5]
panjang = len(kumpulan_angka)
for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# list comprehension
print("\nList Comprehension")
data = ["uti",1,2,3,"padila"]

[print(f"data={i}") for i in data]

angka = [10,5,4,2,6,5]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\nEnumarate")
data_list = ["uti",1,2,3,"padila"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")