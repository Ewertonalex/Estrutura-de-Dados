import numpy as np

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade #capacidade da fila cheia
        self.inicio = 0 #inicio da fila
        self.final = -1 #fim da fila
        self.numero_elementos = 0 #tamanho da fila(0 pq nao está predefinido o tamanho da fila)
        self.valores = np.empty(self.capacidade, dtype=int) #receber os valores

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila está cheia!')
            return
        if self.final == self.capacidade -1:  #saber se a fila está cheia
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor #acrescentar valor a fila
        self.numero_elementos += 1 #enfileirar +1 a fila

    def desinfileirar(self):
        if self.__fila_vazia():  #ver se fila está vazia
            print('A Fila está vazia!')
            return
        temp = self.valores[self.inicio]  #varivael temporaria, para criar um lugar temporario na fila, vai receber um valor temporariamente que estava no inicio
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.numero_elementos = -1   #ver se tem espaço, para retornar para fila o valor que ficou na fila
        return temp

    def primeiro(self): #verificar quem vai ser o primeiro da fila, e retornar o valor da variavel do inicio.
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]