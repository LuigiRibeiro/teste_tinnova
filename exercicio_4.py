# 4 - Somo de multiplos de 3 ou 5

class Multiplos35:
    def somar(self, number):
        resultado = 0

        inc = 0
        while True:
            if inc + 3 < number:
                print(inc + 3)
                inc = inc + 3
                resultado += inc
            else:
                break
        inc = 0
        while True:
            if inc + 5 < number:
                print(inc + 5)
                inc = inc + 5
                resultado += inc
            else:
                break

        return resultado

multiplos = Multiplos35()
print(f'A soma do multiplos 3 e 5 é {multiplos.somar(50)}')
