import os




if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    print("Selamat Datang di Program")
    print("DATABASE PERPUSTAKAAN")
    print("========================")
    

