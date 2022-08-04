nome = str(input('Nome completo: ')).upper().strip()
n1 = nome.split()
print('Seu primeiro nome é: {}.'.format(n1[0]))
print('Seu último nome é: {}'.format(n1[len(n1)-1]))