import numpy as np

list_a = [1, 2, 3,4]
vector_a = np.array(list_a)
#Jika dikuadratin error
print(f"list a= {list_a}")
#Jika dikuadratin bisa karena kan vektor, bukan list 1 dimensi 
print(f"vektor a = {vector_a**2}")
print(f"vektor b = {vector_a*5}")

matrix_c = ([1,2], [3,4])
matrixnya_c = np.array(matrix_c)
print(f"matriks c = \n{matrixnya_c}")
print(f"matriks c * 5 = \n {matrixnya_c*5}")

zeros_c = np.zeros((2,2))
print(f"matriks kosong = \n {zeros_c}")
ones_d = np.ones((2,2))
print(f"matriks satu = \n {ones_d}")
jumlah_matrix =  matrixnya_c + ones_d + matrixnya_c*2
print(f"matriks jumlah = \n {jumlah_matrix}")


