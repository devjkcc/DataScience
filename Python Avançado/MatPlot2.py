import matplotlib.pyplot as plt
import numpy as np
valor = [2,4,6,8,10,12,14,16]
produto=[1,2,3,4,5,6,7,8]
# Usado para criar gráficos de dispersão
plt.scatter(valor,produto)
x = np.arange(0,100,1)
plt.plot(x,x**2)
print(plt.show()) # Gerando um gráfico exponencial