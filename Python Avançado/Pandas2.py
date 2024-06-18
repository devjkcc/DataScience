import pandas as pd

#Gerando tabelas

notas = {'Alunos': ['Bruno', 'João', 'Ana', 'José'], 'Notas': ['10', '7', '10', '4']
         , 'Situação': ['Aprovado', 'Aprovado', 'Aprovado', 'Reprovado']}

tabela = pd.DataFrame(notas)
print(tabela)


print(tabela.describe())
print(tabela['Notas']) # Retorna a coluna notas
print(tabela.loc[[1]]) #Retorna apenas a primeira linha
print(tabela.loc[[0,1]]) #Retorna as linhas 0 e 1
print(tabela.loc[0:3])#Retorna todas as linhas  de 0 a 3
print(tabela.loc[tabela['Notas']=='10']) # Retorna alunos com nota 10