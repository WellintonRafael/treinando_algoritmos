a = (int(input('Digite um número: ')), int(input('Digite um número: ')),
    int(input('Digite um número: ')), int(input('Digite um número: ')))
if 9 in a:
    print(f'O número 9 apareceu {a.count(9)} vezes.')
else:
    print('O número 9 não está na lista.')
if 3 in a:
    print(f'O número 3 está na {a.index(3) + 1}ª posição')
else:
    print('Não foi digitado nenhum número 3.')
print('Os números pares são:')
for x in a:
    if x % 2 == 0:
        print(x, end= ' ')