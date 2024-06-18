import numpy as np
rng = np.random.default_rng() 
#Criando matrizes
a = np.array([[1,2,3], [4,5,6]])
print(a)

b = np.ones((3,3)) # Criando uma matriz 3x3 com numeros 1
print(b)

c = np.zeros((3,3))
print(c)

d = rng.random((3,3))
print(d)

#Retornando valores unicos
e = np.array([1,2,3,4,5])
f = np.array([5,6,7,8,9])

concat = np.concatenate((e,f))

print(np.unique(concat))