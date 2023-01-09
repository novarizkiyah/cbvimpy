from . import Operasi

def update_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor buku yang akan diupdate")
        no_buku = int(input("Nomor buku: "))
        data_buku = Operasi.read(index=no_buku)
    
        if data_buku:
            break
        else:
            print("Nomor tidak valid silahkan masukkan nomor lagi")
        
    data_break = data_buku.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    print(pk)
    print(date_add)
    print(penulis)
    print(judul)
    print(tahun)

def create_console():
    #Header
    print("\n\n"+"="*100)
    print("Silahkan Tambahkan Data Buku\n")
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while(True):
        try:
            tahun = int(input("Tahun: "))
            if len(str(tahun))== 4:
                break
            else:
                print("Tahun harus empat angka")
        except:
            print("Tahun harus angka, silahkan masukkan lagi")
    
    Operasi.create(tahun,judul,penulis)
    print("Berikut adalah data baru Anda\n")
    read_console()

def read_console():
    # print("ini adalah read")
    data_file = Operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    #Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    #Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}")
    #Footer
    print("="*100+"\n")

