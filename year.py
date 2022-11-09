def hari_kabisat(tahun):
    kabisat=False

    if (tahun%4==0):
        kabisat=True
        if(tahun%100==0):
            kabisat=False
            if(tahun%400==0):
                kabisat=True
    else:
        kabisat=False
    return kabisat
tahun = int(input())
print(hari_kabisat(tahun))
