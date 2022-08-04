from math import factorial
n = int(input('Digite um número para ver seu fatorial: '))
c = n
f = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -=1
print(f)
