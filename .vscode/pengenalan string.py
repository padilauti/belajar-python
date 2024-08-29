data = "ini adalah string"
print(data)
print(type(data))

## 1. CARA MEMBUAT STRING
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)
data = "menggunakan double quote"
print(data)

print('"halo, apa kabar?"')
print("'halo, apa kabar?'")
print("hari ini adalah jum'at")

## 2. MENGGUNAKAN TANDA \
# membuat tanda ' menjadi string
print('hari ini adalah hari jum\'at')
print('g\'day, isn\' it?')

# backlash
print("C:\\user\\Padila")

# tab (bikin jarak menjauh)
print("Uti\tNur\tPadila")

# backspace (bikin jarak mendekat)
print("Uti \bNur \bPadila")

#newline
print("baris pertama.\nbaris kedua.") # LF->line feed
print("baris pertama.\rbaris kedua.") # CR -> carriage return
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return

## 3. STRING LITERAL DAN RAW
# hati-hati
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Uti Nur Padila
Kelas : 12 Akuntansi
""")

# multiline literal string dan RAW
print(r"""
Nama : Uti Nur Padila
Kelas : 12 Akuntansi
Website : www.padil.com/newID
""")