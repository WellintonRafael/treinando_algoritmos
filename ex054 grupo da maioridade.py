from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
p = 0
p1 = p =+ 1
pessoas = int(input(f'Ano de nascimento da {p1}ªpessoa: '))
while not pessoas == u'\ue007':
    pessoas = int(input(f'Ano de nascimento da pessoa número {pessoas}: '))
    idade = atual - pessoas
    if idade >= 18:
        totalmaior += 1
    elif idade < 18:
        totalmenor += 1
print('{} pessoas são maiores de idade.'.format(totalmaior))
print('{} pessoas são menores de idade.'.format(totalmenor))
