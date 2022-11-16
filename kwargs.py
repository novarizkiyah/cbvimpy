#kwargs = keywords, argument

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")
fungsi("Aya", 108, 18)

def fungsi(**kwargs):
    '''fungsi kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")
fungsi(nama = "Aya", berat = 108, tinggi = 18) #dictionary

#studi kasus

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] =="tambah":
        for angka in args:
            output +=angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *=angka
    else:
        print("tidak ada operasi")
    return output

hasil = math(1,3,4,option="tambah")
print(f"hasil jumlah {hasil}")

hasil = math(1,3,4, option="kali")
print(f"hasil kali {hasil}")