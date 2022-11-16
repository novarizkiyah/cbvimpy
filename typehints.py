


def fungsi(parameter):
    print(parameter)

fungsi(1)
fungsi("rta")
fungsi(True)

# menjadi masalah karena tipe datanya any, program tetap bisa jalan

def sepuluh_pangkat(argument:int) -> int:
    '''Fungsi dengan Hints'''
    output = 20**argument
    return output
hasil = sepuluh_pangkat(2)
print(hasil)


import string

def studi(nama:string):
    print(nama)
studi("lamana")
#Masih menjadi misteri kenapa ini keluar NovaAryya heraan 