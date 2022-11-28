##Global dan local scope

nama_global = "nova" #<- ini variable global

#akses variable global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama_global}")
fungsi()

#akses variable global dalam loop

for i in range(1,5):
    print(f"loop {i} - {nama_global}")

#percabangan
if True:
    print(f"if menampilkan {nama_global}")

## variabel local scope

def fungsi2():
    nama_local = "Aya" #<- variable local scope
fungsi2()
# print(nama_local) tidak bisa dilakukan

#contoh 1 : penggunaan akses variable
def contoh1():
    print(f"Helllo {nama}")
nama = "Nova"
contoh1()

#contoh 2 : merupakan variabel global
angka =0
def ubah_nilai(angka_baru):
   global angka 
   angka = angka_baru
print(f"angka sebelum {angka}")
ubah_nilai(10)
print(f"angka sesudah {angka}")

#contoh 3 kalau 2 variabel
angka =0
nama = "Aya"
def ubah_nilai(angka_baru, nama_baru ):
   global angka 
   angka = angka_baru
   global nama
   nama = nama_baru
print(f"{nama} punya angka sebelum {angka}")
ubah_nilai(10, "Nova")

print(f"{nama} punya angka sesudah {angka}")

#contoh 4
angka1 = 0

for i in range(0,5):
    angka1 +=i
    angka_dummy = 0
print(angka1)
print(angka_dummy)

if True:
    angka1 = 10
    angka_dummy = 10
print(angka1)
print(angka_dummy)

#global hanya berpengaruh di fungsi