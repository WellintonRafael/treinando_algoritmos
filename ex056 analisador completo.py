maior = 0
menor = 0
soma = 0
homemvelho = ''
maioridadeh = 0
totmulher20 = 0
for c in range(1, 6):
    pessoa = c
    print(('-' * 8), '{}ª PESSOA'.format(pessoa), ('-' * 8))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    if c == 1 and sexo in 'Mm':
        maioridadeh = idade
        homemvelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        homemvelho= nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
    soma += idade
    media = soma / 3
print('O homem mais velho se chama {} e tem {} anos.'.format(homemvelho, maioridadeh))
print('A média de idade do grupo é de {:.0f} anos.'.format(media))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
