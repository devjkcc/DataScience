import pandas as pd
import matplotlib.pyplot as plt

#Mostrando o gráfico de uma tabela
tabela = pd.read_csv('C:/Users/jeffe/OneDrive/Área de Trabalho/Documentos/Python2024/athlete_events.csv')
tabela.hist(column = 'Age', bins=100)
print(plt.show())

tabela.boxplot(column = 'idade')