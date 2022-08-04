from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('A idade do atleta é: {}'.format(idade))
if idade <= 9:
    print('CATEGORIA MIRIM:')
elif idade <= 14:
    print('CATEGORIA INFANTIL:')
elif idade <= 19:
    print('CATEGORIA JÚNIOR:')
elif idade <= 25:
    print('CATEGORIA SÊNIOR:')
else:
    print('CATEGORIA MASTER:')