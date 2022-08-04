print('---' * 20)
num = int(input('Digite um número para descobrir se ele é primo ou não: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print((c), end=' ')
print('\n\033[mO número digitado foi: {}. Ele é divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo.')
