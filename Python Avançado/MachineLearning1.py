import pandas as pd
# Carregando os dados
arquivo = pd.read_csv("C:/Users/jeffe/OneDrive/Área de Trabalho/Documentos/Python2024/wine_dataset.csv")
# Transformando o vinho vermelho por 0
arquivo['style'] = arquivo['style'].replace('red', 0)
#Tranformando o vinho branco por 1
arquivo['style'] = arquivo['style'].replace('white', 1)

y = arquivo['style']
x = arquivo.drop('style', axis = 1)

from sklearn.model_selection import train_test_split # Criando variável para treinar 
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size= 0.3)

from sklearn.ensemble import ExtraTreesClassifier
#Criando o modelo
modelo =  ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

#Imprimindo resultado// Aqui mostra a probabilidade de acerto da máquina
resultado = modelo.score(x_teste, y_teste)
print("Probabilidade" , resultado)

# Verificando o y_teste em determinado intervalo

print(y_teste[500:505])
#Resultado obtido: 1 1 0 1 0
#Verificando o x teste em determinado intervalo

print(x_teste[500:505])
 

#Criando a varíavel para descobrir se a inteligencia vai prever se o vinho é branco ou tinto
previsao = modelo.predict(x_teste[500:505])
print(previsao)
#resultado obtido: 1 1 0 1 0
#Logo, a máquina acertou todos
