v = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco'
usuario = int(input('Digite um número de 0 até 5: '))
while usuario not in range(0, 6):
    usuario = int(input('Opção inválida! Digite um número de 0 até 5: '))
print(f'Você digitou o número {v[usuario]}')
