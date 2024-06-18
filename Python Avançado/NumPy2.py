import numpy as np
#Ordenando um array
a = np.array([5,4,9,11,21,2,1])
print(np.sort(a))
print(np.shape(a))
#Adicionando uma dimensão no array com newaxis
a2 = a[np.newaxis, :]
print(np.shape(a2))
print(np.sort(a2))
#Adicionando uma dimensão com expand_dims(funcionam igual)
a3 = np.expand_dims(a, axis = 1)


b = np.array([40,38,90,23,24,12])
#Concatenando arrays
concatenacao = np.concatenate((a,b))
print(concatenacao)

