# Date and time (latihan)

import datetime as dt
hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")

tanggal = dt.date(2006,7,24)
print(tanggal)
print(f"Hari ini adalah hari = {tanggal:%A}")


print("Silakan masukan tanggal, \nbulan dan tahun lahir anda\n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Hari nya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(umur_hari)
print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")

