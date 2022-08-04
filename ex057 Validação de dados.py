sexo = str(input('Qual seu sexo [M/F]:')).strip().lower()[0]
while sexo not in 'mf':
    print('Opção inválida.')
    sexo = str(input('Digite novamente'))
print('Sexo {} regitrado com sucesso!'.format(sexo))
