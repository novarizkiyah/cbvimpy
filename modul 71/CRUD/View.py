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
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    # print(pk)
    # print(date_add)
    # print(penulis)
    # print(judul)
    # print(tahun)

    #milih mana yang akan diupdate, bikin looping

    while(True):
        print("\n"+"="*100)
        print("Silahkan pilih data apa yang akan diupdate")
        print(f"1. Judul\t:{judul:.40}")
        print(f"2. Penulis\t:{penulis:.40}")
        print(f"3. Tahun\t:{tahun:4}")

        user_option = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        
        match user_option:
            case "1": judul = input("judul\t: ")
            case "2": penulis = input("penulis\t: ")
            case "3": 
                while(True):
                    try:
                        tahun = int(input("Tahun: "))
                        if len(str(tahun))== 4:
                            break
                        else:
                            print("Tahun harus empat angka")
                    except:
                        print("Tahun harus angka, silahkan masukkan lagi")
            case _:print("index tidak cocok")
        
        print("Data baru Anda")
        print(f"1. Judul\t:{judul:.40}")
        print(f"2. Penulis\t:{penulis:.40}")
        print(f"3. Tahun\t:{tahun:4}")

        is_done = input("Apakah data sudah sesuai?(y/n) ")
        if is_done == "y" or is_done == "Y":
            break
    Operasi.update(no_buku,pk,data_add,tahun,judul,penulis)

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
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")
    #Footer
    print("="*100+"\n")

