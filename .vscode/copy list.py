## teknik mendukplikat list

a = ["uti","ipit","april"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

# kita akan merubah member dari a

# ini akan merubah kedua  list
a[1] = "padila"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# mendukplikat list dengan menggunkan list

print("membuat list c dengan a.copy()")
c =a.copy() # full duplikat
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


print("kita ubah data 1")
c[1] = "padil"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 1")
a[1] = "ipit"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

