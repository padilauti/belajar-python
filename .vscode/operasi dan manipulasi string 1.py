## OPERASI DAN MANIPULASI STRING

#  1. menyambung string(concatenate)
nama_pertama = "Uti"
nama_tengah = "Nur"
nama_akhir = "Padila"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir 
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. operator untuk string
# mengecek apakah ada komponen char atau string di string

D = "P"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))

d = "p"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0:2] : " + nama_lengkap[0:3])
print("index ke-[2:6] : " + nama_lengkap[2:7])
print("index ke-[0,2,4,6,8,10,12] : " + nama_lengkap[0:12:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

# 4. operator dalam bentuk method

data = "Uti Nur Padila"
jumlah = data.count("a")
print("jumlah a pada " + data + " = " + str(jumlah ))
