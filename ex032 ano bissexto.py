from datetime import date
ano = int(input('ano que deseja analisar: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('BISSEXTO!')
else:
    print('NÃO É BISSEXTO!')