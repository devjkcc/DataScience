#Adicionando o self
class TestePoo:
    def incrementa(self, v, i):
        self.valor = v
        self.incrementa = i
        self.resultado = self.valor + self.incrementa
        return self.resultado
    
a = TestePoo()
b = a.incrementa(10,5)
print(a.valor)


class TestePoo2:
    def __init__(self, v = 10, i =1):
        self.valor = v
        self.incremento = i
        self.valorExponencial = v
    def incrementa(self):
        self.valor = self.valor + self.incremento
    def verify(self):
        if self.valor > 12:
            print('Ultrapassou 12')
        else:
            print('Tudo ok')
    def exponencial(self,e):
        self.valorExponencial = self.valor**e
    def incrementaQuadrado(self):
        self.incrementa()
        self.exponencial(2)

a = TestePoo2()
a.incrementa()
print(a.valor)
a.verify()
a.exponencial(3)
print(a.valorExponencial)
