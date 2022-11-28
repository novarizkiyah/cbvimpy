'''*args'''
#memasukkan data/argumen

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")
fungsi("Aya", 108, 18)

def nilai(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")
nilai(["Nova",155,42])

#kenalan dengan *args, sama dengan list imputnya bisa kayak paling atas, cara manggil sama seperti yang atas, ndak pake list
def fungsi(*args):
    nama=args[0]
    tinggi= args[1]
    berat=args[2]
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")
fungsi("Aryya", 170, 60)  

#studi kasus input bebas jumlahnya berapa 
def tambah(*data):
    #data tipenya tuple dan bisa diiterasi
    output = 0
    for angka in data:
        output += angka
    return output

hasil= tambah(3,4,5,7,2,5,7,3,6,8,)
print(hasil)

hasil= tambah(3,4,5,7,3,6,8,)
print(hasil)

#kita apunya fungsi yang dinamik, mengambil banyak input