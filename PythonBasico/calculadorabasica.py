def obter_valores():
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    return valor1, valor2

def switch(escolha):
    if escolha == 1:
        valor1, valor2 = obter_valores()
        print("Resultado:", valor1 + valor2)
    elif escolha == 2:
        valor1, valor2 = obter_valores()
        if valor2 > valor1:
            valor1, valor2 = valor2, valor1
        print("Resultado:", valor1 - valor2)
    elif escolha == 3:
        valor1, valor2 = obter_valores()
        print("Resultado:", valor1 * valor2)
    elif escolha == 4:
        valor1, valor2 = obter_valores()
        if valor2 != 0:
            print("Resultado:", valor1 / valor2)
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Opção inválida.")

while True:
    print("[1] - Soma")
    print("[2] - Subtração")
    print("[3] - Multiplicação")
    print("[4] - Divisão")
    
    escolha = input("Escolha uma operação (ou pressione Enter para sair): ")

    if escolha == "":
        break

    try:
        escolha = int(escolha)
        switch(escolha)
    except ValueError:
        print("Por favor, insira um número válido.")

print("Programa encerrado.")
