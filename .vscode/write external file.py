# 1. mode write

# dia akan membuat file baru jika tidak ada
# lalu akan menimpa atau oversize isinya

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("Uti Nur Padila")

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("Muhammad Ilham")

# 2. mode append

with open("data_2.txt",'w',encoding="utf-8") as file:
    file.write("Uti Nur Padila\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("Diah Linggawati\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("Muhammad Ilham")

# 3. mode r+

with open("data_3.txt",'w',encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("baris-1 \n")
    file.write("baris-2 \n")
    file.write("baris-3 \n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("Padil") # akan menimpa isi text


 