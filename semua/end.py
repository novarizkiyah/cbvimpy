#mau buat masukan angka, lalu angkanya jadi string dimulai dari 1
if __name__ == '__main__':
    n = int(input())
    for n in range(1,n+1):
        print(n,end="")

#gunanya end secara default fungsi print() Python diakhiri dengan baris baru. Fungsi print() Python hadir dengan parameter yang disebut 'end'. Secara default, nilai parameter ini adalah '\n', yaitu karakter baris baru. Mengubahnya menjadi "" menghapus karakter baris baru
