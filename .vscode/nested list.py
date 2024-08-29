data_0 = [1,2]
data_1 = [3,4,5]

data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")

list_2D = [data_0,data_1,9,0,8]
print(f"list 2D = {list_2D}")

# contoh penggunaan 

peserta_0 = ["uti",17,"wanita"]
peserta_1 = ["diah",18,"wanita"]
peserta_2 = ["ilham",19,"laki-laki"]
peserta_3 = ["padila",17,"wanita"]

list_peserta = [peserta_0,peserta_1,peserta_2,peserta_3]

print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")

# dengan reference 

list_copy = list_peserta.copy();
print(f"peserta ={list_copy}")
peserta_0[0] = "muhammad"
print(f"peserta = {list_copy}")
print(f"peserta = {list_peserta}")

