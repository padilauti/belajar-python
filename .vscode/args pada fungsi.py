'''*args'''

# memasukan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Uti",162,50)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat= data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
fungsi(["Padila",170,55])

# kenalan dengan *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat= args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Nur",120,120)

# studi kasus

def tambah(*data):
    # data tipenya adalah tuples, dia bisa diliterasikan
    output = 0
    for angka in data:
        output += angka

    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")

hasil = tambah(10,5,15)
print(f"hasil = {hasil}")



