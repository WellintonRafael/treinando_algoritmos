lar = float(input('Digite a largura da parede que pretende pintar (m): '))
alt = float(input('Agora digite a altura (m): '))
ar = lar * alt
tinta = ar / 2.5
print('Área total a ser pintada: {:.1f}m2'.format(ar))
print('Para pintar essa parede, será nescessário {:.1f}litros de tinta!'.format(tinta))