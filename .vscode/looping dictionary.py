# looping dictionary 

teman_teman = {
    "cup":"ucup serucup",
    "tong":"otong surotong",
    "dung":"dudung seruddung",
    "sep":"asep si kasep",
    "cuy":"acuy serucuy"
}

# looping first try (yang kleuar adalah keynya)
for teman in teman_teman:
    print(teman)

# operator untuk mengambil item / iterable
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)

items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)

for key, value in teman_teman.items():
    print(f"key = {key}, value = {value}")