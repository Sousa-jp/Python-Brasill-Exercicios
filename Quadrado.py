"""Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;"""


class Quadrado:

    def __init__(self, lado, unidade):
        self._lado = float(lado)
        self._area = lado**2
        self._unidade = unidade.lower()

    def __str__(self):
        return 'Lado: {} {}, Area: {:.2f}'.format(self._lado,self._unidade,self._area)

    def change_lado(self, novo_lado):
        self._lado = float(novo_lado)
        self._area = self._lado**2

    def retorna_valor_lado(self):
        return self._lado

    def calcula_area(self):
        return "{:.2f}".format(self._area)

quad = Quadrado(8, 'MeTroS')
quad.change_lado(8.99)

area_do_quad = quad.calcula_area()
lado_do_quad = quad.retorna_valor_lado()

print(quad)
