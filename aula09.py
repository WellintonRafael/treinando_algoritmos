nome = str(input('Digite seu nome completo: ')).strip()
n1 = nome.upper()
n2 = nome.lower()
n3 = len(nome)-nome.count(' ')
nome = n1, n2
print('Seu nome em letras maiúsculas é: {}'.format(n1))
print('Seu nome em letras minúsculas é: {}'.format(n2))
print('Seu nome tem {} letras.'.format(n3))