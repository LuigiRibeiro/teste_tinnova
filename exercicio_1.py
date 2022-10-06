# 1 - Votos em relação ao total de eleitores

class Votos:
    def __init__(self):
        self.total_eleitores = 1000
        self.validos = 800
        self.votos_brancos = 150
        self.nulos = 50

    def percetual_validos(self):
        print(f'O percuntual de votos válido é {self.validos / self.total_eleitores * 100}%')

    def percetual_brancos(self):
        print(f'O percuntual de votos em branco é {self.votos_brancos / self.total_eleitores * 100}%')

    def percetual_nulos(self):
        print(f'O percuntual de votos válido é {self.nulos / self.total_eleitores * 100}%')


votos = Votos()
votos.percetual_validos()
votos.percetual_brancos()
votos.percetual_nulos()