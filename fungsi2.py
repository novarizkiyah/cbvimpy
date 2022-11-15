

def panggil(nama):
    print(f"Selamat datang {nama}")

panggil("Nova")
panggil("Aya")

def tambah(angka_1, angka_2):
    hasil = angka_1+angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")
tambah(7,9)
tambah(9,130)

def sapaan(list_peserta):
    data_peserta=list_peserta.copy()
    for peserta in data_peserta:
        print(f"Halo, Selamat Datang {peserta}")

grub= ["Nova", "Aryya", "Aya", "Yusril"]

sapaan(grub)