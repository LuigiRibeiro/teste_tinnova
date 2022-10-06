# 2 - Algoritmo de orientação Bubble Sort

class BlubbleSort:
    def __init__(self, vector):
        self.vector = vector

    def ordenar(self):
        print(f'Ordenar o vetor {self.vector}')

        for i in range(0, len(self.vector) - 1):
            for j in range(0, len(self.vector) - 1 - i):
                if self.vector[j] > self.vector[j + 1]:
                    num_troca = self.vector[j + 1]
                    self.vector[j + 1] = self.vector[j]
                    self.vector[j] = num_troca

        print(f'Vetor ordenado {self.vector}')


blubble = BlubbleSort([9, 8, 5, 6, 3, 0, 1, 2, 4, 7])
blubble.ordenar()