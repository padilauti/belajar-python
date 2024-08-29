import sainss
from sainss.matematika import scientific

hasil_tambah = sainss.matematika.tambah(1,2,3,4,45)
print(f"hasil tambah = {hasil_tambah}")

hasil_fisika = sainss.fisika.gaya(10,9.8)
print(f"hasil fisika = {hasil_fisika}")

hasil_kali = sainss.matematika.kali(1,3,4,5,6)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = scientific.pangkat(3)
print(f"hasil pangkat 3 = {pangkat_3(5)}")
