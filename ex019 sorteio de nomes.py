from random import choice
from time import sleep
n1 = str(input('Nome 01: '))
n2 = str(input('Nome 02: '))
n3 = str(input('Nome 03: '))
n4 = str(input('Nome 04: '))
n5 = str(input('Nome 05: '))
lista = [n1, n2, n3, n4, n5]
print('O Sorteado 1 foi: {}'.format(choice(lista)))
