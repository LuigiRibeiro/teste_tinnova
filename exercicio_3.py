# 3 - Fatorial

class Fatorial:
    def calcular(self, numero):
        print(f'Calcuar o fatorial de  {numero}')

        if numero > 0:
            resultado = 1
            inc = 1
            while inc <= numero:
                resultado *= inc
                inc += 1
            print(f'O fatorial é {resultado}')
        elif numero == 0:
            print(f'O fatorial é 1')
        else:
            print(f'Escolha um numero natural')

fatorial = Fatorial()
fatorial.calcular(0)
fatorial.calcular(1)
fatorial.calcular(2)
fatorial.calcular(3)
fatorial.calcular(365)
fatorial.calcular(-1)