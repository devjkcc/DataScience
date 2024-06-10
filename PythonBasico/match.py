# A estrutura match funciona como um switch case de outras linguagens

print("[1] - Para dizer olá")
print("[2] - Para perguntar seu nome")
escolha = int(input())
def switch(escolha):
    match escolha:
     case 1:
            print("Olá")
     case 2:
            nome = input(print("Qual seu nome?"))
     case _:
            print("Algo deu errado")
switch(escolha)
