bebidas = 'guaraná', 'suco', 'água', 'café', 'leite'

pedido = str(input('Qual será seu pedido hoje? '))
#while pedido not in u'\ue007':
    #pedido = str(input('Mais alguma coisa? '))
for c in bebidas:
    print(pedido, end= ' - ')
