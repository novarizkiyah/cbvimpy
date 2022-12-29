
with open("data_1.txt", "w", encoding="UTF-8") as file:
    file.write("Nova Berani Wkkwkwkw")

with open("data_1.txt", "w", encoding="UTF-8") as file:
    file.write("Aryya ganteng Wkkwkwkw")

with open("data_1.txt", "w", encoding="UTF-8") as file:
    file.write("Aya Berani Wkkwkwkw")

#semuanya akan ketimpa yang paling belakang

##2 maka pake append
with open("data_2.txt", "w", encoding="UTF-8") as file:
    file.write("Aya Berani 1 Wkkwkwkw\n")
with open("data_2.txt", "a", encoding="UTF-8") as file:
    file.write("Aya Berani 2 Wkkwkwkw\n")
with open("data_2.txt", "a", encoding="UTF-8") as file:
    file.write("Aya Berani 3 Wkkwkwkw\n")

##2 maka pake r+
with open("data_3.txt", "w", encoding="UTF-8") as file:
    file.write("Data ke-3\n")
with open("data_3.txt", "r+", encoding="UTF-8") as file:
    file.write("Baris ke-1\n")
    file.write("Baris ke-2\n")
    file.write("Baris ke-3\n")
with open("data_3.txt", "r+", encoding="UTF-8") as file:
    data = file.read()
    print(data)
with open("data_3.txt", "r+", encoding="UTF-8") as file:
    file.write("Baris\n") #Menimpa isi text sesuai panjang data