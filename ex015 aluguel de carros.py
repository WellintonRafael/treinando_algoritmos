d = int(input('Por quantos dias pretende utilizar o veículo? '))
km = float(input('Quantos kilômetros pretende andar com o veículo? '))
vd = d*60
vkm = km*0.15
print('Valor total a pagar será: R$ {:.2f}'.format(vd+vkm))