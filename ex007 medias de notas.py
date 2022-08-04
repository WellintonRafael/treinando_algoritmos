n1 = float(input('Nota da prova: '))
n2 = float(input('Nota dos exercícios: '))
n3 = float(input('Nota da redação: '))
n4 = float(input('Nota do trabalho: '))
s = (n1 + n2 + n3 + n4) / 4
if s >= 7:
    print('Sua média final é: {:.2f} e você foi APROVADO!!!' .format(s))
elif s >= 5 and s < 7:
    print('Sua média final foi {:.2f}, portanto deverá ficar de RECUPERAÇÃO!'.format(s))
else:
    print('Sua média foi {:.2f} e infelizmente você foi reprovado!'.format(s))
