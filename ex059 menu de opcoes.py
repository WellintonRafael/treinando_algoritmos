n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = 0
soma = n1 + n2
while n3 != 4:
    n3 = int(input('O que quer fazer agora? \n '
                   '1-Somar, 2-Outra operação, 3-Novos valores, ou 4-Sair? '))
    if n3 == 1:
        print(soma)
    elif n3 == 3:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        n3 = int(input('Oque quer fazer agora? \n '
                       '1-Somar, 2-Outra operação, 3-Novos valores, ou 4-Sair? '))
    else:
        print('Opção inválida!')
print('Falou... Até mais!')
