# Classes, objetos, Metodos, Herança, Construtor

def teste(v,i):
    valor = v
    incremento = i
    resultado = valor + incremento
    return resultado

a = teste(50,20)
print(a)

# Dentro da classe é possivel colocar várias funções
class TestePoo:
    def incrementa(self, v, i):
        valor = v
        incrementa = i
        resultado = valor + incrementa
        return resultado

b = TestePoo()
c = b.incrementa(10,5)
print(c)
