import os

# program untuk menghitung luas dan keliling
# Membuat header program

# os.system("clear")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# #Mengambil input user
# LEBAR = int(input("Masukkan nilai lebar: "))
# PANJANG = int(input("Masukkan nilai panjang: "))

# #Program menghitung luas
# LUAS= PANJANG*LEBAR
# KELILING=2*(PANJANG+LEBAR)
# print(f"Nilai luas:{LUAS}")
# print(f"Nilai keliling: {KELILING}")

def header():
    '''fungsi Header'''
    os.system("clear")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")
def input_user():
    '''fungsi input user'''
    lebar = int(input("Masukkan nilai lebar: "))
    panjang = int(input("Masukkan nilai panjang: "))
    return lebar, panjang

def hitung_luas(lebar, panjang):
    '''fungsi luas'''
    return lebar*panjang
def hitung_keliling(lebar, panjang):
    '''fungsi keliling'''
    return 2*(panjang+lebar)
def display(message, value):
    '''fungsi display'''
    print(f"hasil perhitungan {message} = {value}")

#Program utamanya

while True:
    header()
    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)

    display("luas", LUAS)
    display("keliling", KELILING)
    isContinue = input("apakah mau lanjut(y/n)?")
    if isContinue == "n":
        break
print("Program selesai, terima kasih")