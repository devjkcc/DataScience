import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

tabela = pd.read_csv('C:/Users/jeffe/OneDrive/Área de Trabalho/Documentos/Python2024/athlete_events.csv')
tabela['Medal'].fillna('Zero', inplace = True) # Transformando os dados nulos em zero
tabela2 = tabela.dropna() # Remover dados nulo