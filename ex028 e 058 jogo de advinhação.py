from random import randint
from time import sleep
pc = randint(0, 10)
print('-'*50)
print('Vou pensar em um número de 0 a 10!!! Tente advinhar...')
print('-='*20)
stop = False
palpite = 0
while not stop:
    jogador = int(input('Qual é seu palpite?'))
    palpite +=1
    if jogador == pc:
        stop = True
    else:
        if jogador > pc:
            print('Menos')
        elif jogador < pc:
            print('Mais')
print('Acertou com {} palpites.'.format(palpite))