# __main__ adalah top level code environment

#di c/c++
#int main(){
#
#}

#di java
#class Main(){
#    static void main(){
#    }
# }

# __name__ = __main__ akan terjadi jika ada di program utama



print(f"nilai name pada fungsi main_app.py= {__name__}")
import fungsi
#contoh penggunaan
#deklarasi
def tambah(a:int, b:int)-> int:
    return a+b

#fungsi utama

if __name__ == "__main__":
    angka1 = 4
    angka2 = 8
    hasil = tambah(angka1, angka2)
    print(f"Hasil tambah = {hasil}")

import package