preco = float(input('Preço do produto: R$ '))
precofinal = preco - (preco*15/100)
print('Esse produto está com 15% de desconto!')
print('Valor com desconto: R${:.2f}'.format(precofinal))