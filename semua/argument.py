#Argument gunanya untuk menghitung misal di dalam function ada yang diganti
#contoh1
def sapa_kabar(nama="Nova"):
    print(f"Apa Kabar {nama}")
sapa_kabar("Aya")
sapa_kabar()

#contoh2
def salam(nama, pesan = "Assalamualaikum"):
    print(f"{pesan}, {nama}")

salam("Juju", "Hai Anak Baik")
salam("Aryya")

#contoh3
def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil
print(hitung_pangkat(2,3))
print(hitung_pangkat(pangkat=3, angka=6))

#contoh4
def tambah(input1=4, input2=4, input3=9, input4=10):
    hasil=input1+input2+input3+input4
    return hasil
print(tambah())
print(tambah(input3=8))