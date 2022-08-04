l1 = float(input('Medida do lado 1: '))
l2 = float(input('Medida do lado 2: '))
l3 = float(input('Medida do lado 3: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É POSSÍVEL FORMAR UM TRIÂNGULO ', end = '')
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    if l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('NÂO É POSSÍVEL FORMAR UM TRIÂNGULO!')