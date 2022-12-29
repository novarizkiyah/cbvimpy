## tutorial membaca eksternal

print(3*"=", "Membaca file txt dengan bhaique", 3*"=")
file= open("data.txt", mode="r")

print(f"Status readable = {file.readable()}")
print(f"Status writable = {file.writable()}")

#baca seluruh file
print(file.read())

# print(file.readline(),end="") #baca baris pertama
# print(file.readline(),end="")

#baca semua baris sebagai list
#print(file.readlines())

print(f"Apalah file sudah closed = {file.closed}")
file.close()
print(f"Apalah file sudah closed = {file.closed}")

##salah satu cara untuk membuka file di python

print(3*"=", "Membaca file txt dengan with", 3*"=")
with open("data.txt", mode="r") as file:
    content = file.read()
    print(content, end="\n")
    print(f"Apakah sudah diclose ={file.closed}")

print(f"Apakah sudah diclose ={file.closed}")
