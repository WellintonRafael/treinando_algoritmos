t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
p = t + (11 - 1) * r
for c in range(t, p, r):
    print((c), end='  ')
print('PRONTINHO!')
