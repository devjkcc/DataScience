import time

contador = 0
while contador < 5:
    print("carregando")
    contador += 1
    time.sleep(1)

numero = int(input("Digite um valor"))
fatorial = numero
contador2 = 1
while(numero - contador2)>1:
  fatorial = fatorial*(numero-contador2)
  contador2+=1
print('{0}!={1}'.format(numero, fatorial))
