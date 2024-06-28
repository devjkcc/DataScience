from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from typing import List

num_friends = [100, 99, 98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79, 33, 40, 40, 25, 37, 10, 11, 15, 19, 21, 34, 53, 67, 68,74, 70]
friend_counts = Counter(num_friends)
xs = range(101)

ys = [friend_counts[x] for x in xs]
plt.bar(xs,ys)
plt.axis([0,101,0,25])


#Analise estatística
# Verificando a quantidade de amigos
num_points = len(num_friends)
print(num_points)

menorValor = min(num_friends) # Buscando o menor valor
maiorValor = max(num_friends) # Buscando o maior valor
media = np.mean(num_friends) # Buscando a média de valores
print(menorValor)
print(maiorValor)
print(media)

# Função para calcular mediana com listas impares
def _median_odd(xs: List[float]) -> float:
   if(len(xs)%2 != 0):
     return sorted(xs)[len(xs)//2]
# Função para calcular mediana com listas pares   
def _median_even(xs:List[float]) -> float:
   if(len(xs)%2==0):
      sorted_xs = sorted(xs)
      hi_midpoint = len(xs)//2
      return (sorted_xs[hi_midpoint-1] + sorted_xs[hi_midpoint])/2
#Função para unir as duas   
def median(v:List[float]) -> float:
   return _median_even(v) if len(v) %2 == 0 else _median_odd(v)

assert median ([1,10,2,9,5]) == 5
assert median  ([1,9,2,10]) == (2+9)/2

#Função para calcular a moda
def mode(x:List[float]) -> List[float]:
   counts = Counter(x)
   max_count = max(counts.values())
   return [x_i for x_i, count in counts.items()
           if count == max_count]

assert set(mode(num_friends)) == {40}
print(median(num_friends))
print(mode(num_friends))