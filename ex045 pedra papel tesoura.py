from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('Qal é a sua jogada? '))
print('JO....')
sleep(1)
print('KEN....')
sleep(1)
print('POH!!!')
sleep(1)
print('--' * 60)
print('Você jogou {}.'.format(itens[jog]))
sleep(1)
print('O PC jogou {}.'.format(itens[pc]))
sleep(1)
if jog == 0:
    if pc == 0:
        print('          EMPATE!')
    elif pc == 1:
        print('          Você perdeu!   :(')
    elif pc == 2:
        print('          VOCÊ GANHOU!!!   \o/')
elif jog == 1:
    if pc == 0:
        print('          VOCÊ GANHOU!!!   \o/')
    elif pc == 1:
        print('          EMPATE!!!')
    elif pc == 2:
        print('          Você perdeu!   :(')
elif jog == 2:
    if pc == 0:
        print('          Você perdeu!   :(')
    elif pc == 1:
        print('          VOCÊ GANHOU!!!   \O/')
    elif pc == 2:
        print('          EMPATE!')
