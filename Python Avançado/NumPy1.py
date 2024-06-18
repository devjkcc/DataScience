import numpy as np

a = np.array([1,2,3])

print(a)
#Criando uma matriz com numpy
b = np.array([[1,2,3], [4,5,6], [7,8,9]])
array_3d = np.array([[[1, 2.1], [3, 4]], [[5, 6], [7, 8]]])
print(b)
print(b.ndim) # retorna a quantidade de dimensões da matriz(2)
print(b.shape) # Retorna o tipo da matriz(3x3)
print(array_3d) 
print(array_3d.ndim) # 3 dimensões
print(b.size) #Quantidade de elementos da matriz
print(b.dtype) # Retorna o tipo de variavel que a matriz possui(Nesse caso é uma matriz de int)
print(array_3d.dtype) #Nesse caso, é uma matriz de float

f = np.empty(3) #cria uma matriz com valores aleatórios
print(f)

#numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
#Sintaxe padrão para criar listas estilizadas

g = np.arange(2,7,1, int) #começa com o numero 2, vai ate o 7, pulando de 1 em 1, sendo do tipo inteiro
print(g)

h = np.linspace(0,10, num = 5) # O linspace cria uma sequencia float, baseada no numero start, no numero end, e na quantidade de subdivisões, nesse caso ele divide 10 por 5-1
print(h)
