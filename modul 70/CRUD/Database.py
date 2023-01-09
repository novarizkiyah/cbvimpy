
#from signal import pause
from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}

def init_console():
    # print("megecek database")
    # user_str = input("pause")
    try:
        with open(DB_NAME,"r") as file:
            print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        Operasi.create_first_data()
        # with open(DB_NAME,"w",encoding="utf-8") as file:
        #     penulis = input("Penulis: ")
        #     judul = input("Judul: ")
        #     tahun = input("Tahun: ")
            #data_str = f"{penulis},{judul},{tahun}"
            #file.write(data_str)