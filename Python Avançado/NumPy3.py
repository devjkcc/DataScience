import numpy as np

#criando uma seção de um array

a = np.array([1,2,3,4,5,6,7,8])
a2 = a[2:7]
print(a2)

#vstack -> une arrays verticalmente
#hstach -> une arrays horizontalmente

b = np.array([10,22,33,44,55,66,77,88])
print(np.vstack((a,b)))
print(np.hstack((a,b)))