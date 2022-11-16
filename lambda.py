#Lambda function

def f_kuadrat(angka):
    return angka**2
print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# coba lambda function
# output = lambda argument:
kuadrat =lambda angka:angka**2
print(f"Hasil lambda kuadrat = {kuadrat(5)}")

pangkat = lambda num, pow : num**pow
print(f"Hasil lambda pangkat = {pangkat(4,2)}")

##kegunaannya apa sih?

#sorting list biasa
data_list = ["Nova", "Aya", "Aryya"]
data_list.sort()
print(f"sort list ={data_list}")

#sorting list berdasarkan panjang nama
data_list.sort(key=len)
print(f"Sorted list by len {data_list}")

#sorting list berdasarkan panjang nama dengan fungsi
def panjang_nama(nama):
    return len(nama)
data_list.sort(key=panjang_nama)
print(f"Sorted list by len {data_list}")

#sort pakai lambda
data_list.sort(key=lambda nama:len(nama))
print(f"Sorted list by lambda {data_list}")

#filter 
data_angka = [1,4,5,7,43,5,6,7,3, 3, 4, 10,6]
def kurang_dari_lima(angka):
    return angka < 5
data_angka_baru = list(filter(kurang_dari_lima, data_angka))
print(f"Data filter biasa {data_angka_baru}")

#filter pakai lambda
data_angka_baru2 = list(filter(lambda x:x<5, data_angka))
print(f"Data filter pakai lambda {data_angka_baru2}")

#Kasus genap
data_angka_genap = list(filter(lambda x:x%2==0, data_angka))
print(f"Data angka genap filter lambda {data_angka_genap}")

#Kasus ganjil
data_angka_ganjil = list(filter(lambda x:x%2!=0, data_angka))
print(f"Data angka ganjil filter lambda {data_angka_ganjil}")

#kelipatan tiga
data_angka_kelipatan_tiga = list(filter(lambda x:x%3==0, data_angka))
print(f"Data angka ganjil filter lambda {data_angka_kelipatan_tiga}")

# anonymous function
# currying <- Haskell Curry

def pangkat(angka, n):
    hasil = angka**n
    return hasil
data_hasil = pangkat(5,2)
print(f"fungsi biasa = {data_hasil}")

# dengan curying menjadi 

def pangkatx(n):
    return lambda nilai:nilai**n
pangkat2 = pangkatx(3)
print(f"nilai pangkat dua adalah {pangkat2(2)}")
pangkat3 = pangkatx(4)
print(f"nilai pangkat dua adalah {pangkat3(3)}")
print(f"Pangkat bebas adalah {pangkatx(2)(4)}")