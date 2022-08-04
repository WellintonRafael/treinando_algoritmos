print('-='*30)
print('Avaliação de crédito imobiliário!')
renda = float(input('Digite o valor de sua renda familiar: '))
imovel = float(input('Qual o valor do imóvel? '))
anos = int(input('Em quantos anos deseja pagar esse imóvel? '))
meses = anos * 12
vlmensal = imovel / meses
renda30 = renda / 100 * 30
print('Valor da parcela: {:.2f}'.format(imovel/meses))
if vlmensal > renda30:
    print('-='*30)
    print('DESCULPE!\nSeu crédito não foi aprovado, pois o valor da parcela está ultrapassando 30% de sua renda mensal.')
else:
    print('-='*30)
    print('PARABÉNS!!! Seu crédito foi aprovado!')
