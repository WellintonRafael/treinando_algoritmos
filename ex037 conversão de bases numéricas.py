print('-='*35)
print('Conversão de números!')
print('-='*35)
num = int(input('Digite o número que deseja fazer a conversão: '))
print('Digite a opçao desejada:\n'
'[ 1 ] Para BINÁRIO.\n'
'[ 2 ] Para HEXADECIMAL\n'
'[ 3 ] Para OCTAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('A conversão de {} para BINÁRIOS é: {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('A conversão de {} para HEXADECIMAL é: {}.'.format(num, hex(num)[2:]))
elif opcao == 3:
    print('A conversão de {} para OCTAL é: {}'.format(num, oct(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')