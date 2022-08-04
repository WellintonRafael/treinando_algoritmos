sal = float(input('Qual é seu salário atual? '))
aum1 = sal + sal*15/100
aum2 = sal + sal*10/100
aum3 = sal + sal*12.5/100
if sal <= 2000:
    print('Seu aumento será de 15%!\nE seu salário agora é: R${:.2f}'.format(aum1))
if sal <= 5000:
    print('Seu aumento será de 12.5%!\nE seu salário agora é: {:.2f}'.format(aum3))
else:
    print('Seu aumento será de 10%!\nE seu salário agora é: R${:.2f}'.format(aum2))