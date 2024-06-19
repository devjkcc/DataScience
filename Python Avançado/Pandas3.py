import pandas as pd

tabela = pd.read_csv('C:/Users/jeffe/OneDrive/Área de Trabalho/Documentos/Python2024/athlete_events.csv')
print(tabela.head(5))
#Mudando o nome das colunas da tabela
#O inplace = True, significa q ele não vai mostrar a tabela depois de alterar
tabela.rename(columns={'Name': 'Nome', 'Sex': 'Sexo', 'Age': 'idade', 'Height': 'Altura', 'Weight': 'peso', 'Team': 'Time',
                       'NOC': 'Sigla', 'Games': 'Jogos', 'Year': 'Ano', 'Season': 'Temporada', 'City': 'Cidade', 'Sport': 'Esporte'
                       , 'Event': 'Evento', 'Medal': 'Medalha'}, inplace=True)
tabela['idade'] # Mostra a tabela idade

tabela['Medalhas'].value_counts() # Vai contar a quantidade de medalhas