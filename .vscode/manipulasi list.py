## Operasi

# index 0(-3)  1(-2)   2(-3)
data = ["uti","nur","padila"]

# mengambil data dari list ini 
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_uti = data[-3]
print(f"data uti = {data_uti}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## MANIPULASI DATA LIST

#menambahkan item pada list sesuai posisi
print(f"data sebelum di tambah = \n{data}")

data.insert(1,"Aini")
print(f"data sesudah ditambah = \n{data}")
 
# menambah di akhir list
data.append("sujar")
print(f"data ditambah lagi = \n{data}")

# menambahkan list dengan list 
data_baru = ["Ipit","Diah","April"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita ubah data 2 menjadi ilham
data[2] = "ilham"
print(f"data rubah = \n{data}")

# meremove data 
data.remove("sujar")
print(f"data remove = \n{data}")

# data.remove akan eror karena data tidak sesuai, huruf kapital nya harus sesuai

# meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = \n{data}")
print(data_akhir)

