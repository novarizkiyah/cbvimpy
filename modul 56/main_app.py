import sains.matematika
from sains import fisika  #bisa juga ditulis seperti ini
from sains.fisika import gaya as force

hasil_tambah = sains.matematika.tambah(1,2,3,45,)
hasil_kali= sains.matematika.kali(5,2,4)
hasil_pangkat= sains.matematika.pangkat(4)
gaya = fisika.gaya(7,2)

gaya2= force(5,9)

print(hasil_tambah)
print(hasil_kali)
print(hasil_pangkat(2))
print(gaya)
print(gaya2)