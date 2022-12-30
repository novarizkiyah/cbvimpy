#exception akan terjadi saat program mengalami error saat runtime
from math import nan

#contoh pake try
# input_user = int(input("Masukkan angka : "))
# nilai = nan
# try:
#     nilai = 10/input_user
# except:
#     print("Nilai tidak boleh 0")

# print(f"Nilai = {nilai}")

while(True):
    angka = int(input("Masukkan angka : "))
    try: 
        hasil = 10/angka
        print(f"Hasil = {hasil}")
        is_done = input("lanjutkan? (y/n)")
        if is_done == "n":
            break
    except:
        print("Pembagi nol, silahkan masukkan input lagi")
print("Terima kasih sudah mencoba Program 1!")

#Program 2

try:
    with open("data.txt",'r') as file:
        print(file.read())
except:
    print("file data.txt tidak ditemukan, sedang membuat file baru")
    with open("data.txt",'w',encoding="UTF-8") as file:
        file.write("file baru ni bosque")
print("Akhir dari program 2")
