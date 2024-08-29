## OPERASI ARITMATIKA

a = 10
b = 3

# Operasi Tambahan +
hasil = a + b
print(a,'+',b,'=',hasil)

# Operasi Pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

# Operasi Perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# Operasi Pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# Operasi Exsponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# Operasi Modulus (sisa pembagian) %
hasil = a % b
print(a,'%',b,'=',hasil)

# Operasi Floor Division (hasil pembulatan) //
hasil = a // b
print(a,'//',b,'=',hasil)

## PRIORITAS OPERASI, OPERATIONAL PRECEDENCE
'''
    1. ()
    2. Eksponen
    3. Perkalian,Pembagian,modulus, dan floor
    4. Petambahan dan Pengurangan
'''
x = 3
y = 2
z = 4
hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

# kurung bisa di dahulukan
hasil = (x + y) * z
print(x,'+',y,'*',z,'=',hasil)