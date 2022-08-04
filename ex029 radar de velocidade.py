vel = int(input('Qual sua velocidade? '))
multa = (vel - 80) * 7
if vel <= 80:
    print('Boa viagem!')
else:
    print('MULTADO! Valor da multa R$ {}'.format(multa))