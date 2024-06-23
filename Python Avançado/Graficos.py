import matplotlib.pyplot as plt
import numpy as np

figura = plt.figure(figsize=(10,10)) # Definindo o tamanho dos gráficos
# Criando um grafico 
x = np.arange(-1000,1000,1)

#Criando multiplos gráficos

y1 = x**2
# 2 linhas, 2 colunas, e esse grafico vai ficar no primeiro quadrante
plt.subplot(2,2,1)
plt.plot(x,y1)


y2 = x**3
# 2 linhas, 2 colunas, e esse grafico vai ficar no segundo quadrante quadrante
plt.subplot(2,2,2)
plt.plot(x,y2)


y3 = x+2
# 2 linhas, 2 colunas, e esse grafico vai ficar no terceiro quadrante quadrante
plt.subplot(2,2,3)
plt.plot(x,y3)


y4 = -x**2
# 2 linhas, 2 colunas, e esse grafico vai ficar no quarto quadrante quadrante
plt.subplot(2,2,4)
plt.plot(x,y4)

plt.show()