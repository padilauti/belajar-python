## PROGRAM LIST BUKU

list_buku = []
while True:
    print("\nMasukan data buku")
    judul = input("Judul buku\t: ")
    penulis = input("Nama penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    
    print("\n\n","="*10,"Data Buku","="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n\n","="*20)
    islanjut = input("Apakah dilanjutkan?(y/n)")

    if islanjut == "n":
        break

print("PROGRAM SELESAI")