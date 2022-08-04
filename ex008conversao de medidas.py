medida = float(input('Digite uma medida em kilômetros: '))
m = medida * 1000
cm = medida * 10000
mm = medida * 100000
print('{:.0f} metros.'.format(m))
print('{:.0f} centímetros.'.format(cm))
print('{:.0f} milímetros.'.format(mm))