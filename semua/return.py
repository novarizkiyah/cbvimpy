
def kuadrat(input_angka):
    hasil= input_angka**2
    return hasil
y = kuadrat(6)
print(y)
print(kuadrat(y))
z = 10 + kuadrat(3)
print(z)

def fungsi_tambah(angka_1, angka_2):
    return angka_1 + angka_2
m = fungsi_tambah(5,9)
print(m)

def operasi_matematika(angka_1, angka_2):
    tambah = angka_1+angka_2
    kurang = angka_1-angka_2
    kali= angka_1*angka_2
    bagi= angka_1/angka_2
    sisa= angka_1%angka_2

    return tambah, kurang, kali, bagi, sisa
b, c, d, e, f = operasi_matematika(10,3)
print(b)
print(c)
print(d)
print(e)
print(f)