print('-' * 70)
print('!!!VAMOS CALCULAR SEU ÍNDICE DE MASSA CORPORAL (IMC)!!!')
peso = float(input('Qual seu peso? '))
alt = float(input('Qual sua altura? '))
imc = peso / (alt * alt)
print('Seu IMC é: {:.2f}'. format(imc))
if imc <= 18.5:
    print('Seu IMC está baixo! Você está muito magro!')
elif imc <= 24.9:
    print('Seu IMC está normal!')
elif imc <= 29.9:
    print('Seu IMC está alto! Você está em sobrebeso!')
elif imc <= 34.9:
    print('Você está com obesidade (Grau 1)!')
elif imc <= 39.9:
    print('Você está com obesidade severa (Grau 2)!')
else:
    print('Obesidade morbida (Grau 3)!')
print(imc)