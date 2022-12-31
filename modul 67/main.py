import os




if __name__ == "__main__":
    sistem_operasi = os.name

    

    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("Selamat Datang di Program")
        print("DATABASE PERPUSTAKAAN")
        print("========================")

        print(f"1. Read Data")
        print(f"2. Creat Data")
        print(f"3. Update Data")
        print(f"4. Delete Data")

        user_option = input("Masukkan opsi: ")
    

