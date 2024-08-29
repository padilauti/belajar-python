# operator dictionary

data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung serudung"
}

# panjang dictionary 
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak 
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan")) # cek key dengan mesage tidak ditemukan 

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
 
# menambahkan data baru
data_dict["sep"] = "asep si kasep"
print(data_dict)

data_dict.update({"cup":"ucup serucup"})
print(data_dict)
data_dict.update({"padil":"padila si keren"}) # kalau gak ada di add ajah 
print(data_dict)

# mendelete data pada dictionary
del data_dict["padil"]
print(data_dict)