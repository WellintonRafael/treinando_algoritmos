from math import hypot
co = float(input('Digite o quadrado oposto: '))
ca = float(input('Digite o valor do quadrado adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa é: {:.2f}'.format(hip))