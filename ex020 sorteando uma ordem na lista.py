from random import shuffle
from random import choice
n1 = str(input('Nome 1: '))
n2 = str(input('Nome 2: '))
n3 = str(input('Nome 3: '))
lista = [n1, n2, n3]
nome1 = list(shuffle(lista))
nome2 = choice(shuffle(lista))
nome3 = choice(shuffle(lista))
print('A ordem sorteada foi: {} '.format(nome1))
print(nome2)
print(nome3)

