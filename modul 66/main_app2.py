#contoh membuat exception

from numbers import Number

def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "input harus angka"
    return a
print(tambah(5,8))

#Cara bikin exception
angka = 0
# try:
#     hasil =10/angka
# except Exception as error_message:
#     print(error_message)

#atau

try:
    hasil =10/angka
except ZeroDivisionError as error_message:
    print(error_message)
