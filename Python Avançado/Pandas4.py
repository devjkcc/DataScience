import pandas as pd

tabela = pd.read_csv('C:/Users/jeffe/OneDrive/Área de Trabalho/Documentos/Python2024/athlete_events.csv')
#Retirando a coluna id da tabela e sigla
tabela.drop('ID', axis = 1, inplace = True)
tabela.drop('Sigla', axis = 1, inplace = True)