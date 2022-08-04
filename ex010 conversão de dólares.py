vl = float(input('Qual valor você tem na carteira agora(em reais)? R$: '))
dol = vl / 5.37
euro = vl / 6.47
print('Com R${} você pode comprar $ {:.2f} dólares ou $ {:.2f} euros '.format(vl, dol, euro))