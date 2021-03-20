""" Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor """


class Bola:
    def __init__(self, cor, raio, material):
        self.cor = cor
        self._raio = raio
        self.circunferencia = 2 * raio * 3.14
        self.material = material


    def __str__(self):
        return f'Cor: {self.cor}, Circunferencia: {round(self.circunferencia)} m, Material: {self.material}'

    def __eq__(self, other):
        return self.circunferencia == other.circunferencia and self.cor == other.cor and self.material == other.material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        return f'Cor: {self.cor}'

bola = Bola('verde', 5, 'borracha')

bola2 = Bola('verde', 5, 'borracha')

print(bola == bola2)

bola2.trocaCor('azul')

bola2.mostraCor()
