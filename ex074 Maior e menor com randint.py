from random import randint
a = []
for n in range(0, 10):
    a.append(randint(0, 10))
for item in a:
    print(item, end=' ')
print(f'\nO maior valor é {max(a)}')
print(f'E o menor é {min(a)}')
