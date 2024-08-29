data_angka =[1,5,1,4,3,2,4,3,2,3,3,7,8]
print(f"data angka = \n{data_angka}")

# count data 
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data 
data = ["uti","padila","ipit","april"]
print(f"data = {data}")

index_padila = data.index("padila")
index_ipit = data.index("ipit")
print(f"index si padila = {index_padila}")
print(f"index si ipit = {index_ipit}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")

