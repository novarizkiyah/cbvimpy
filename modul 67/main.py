import os
import CRUD as CRUD




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
        
        print("\n========================\n")

        match user_option:
            case "1": print("Read Data")
            case "2": print("Creat Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")

        print("\n========================\n")
        is_done = input("Apakah sudah selesai?(y/n) ")
        if is_done == "y" or is_done == "Y":
            break
    print("Program berakhir, terima kasih :D")


    

