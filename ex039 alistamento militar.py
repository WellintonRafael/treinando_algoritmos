from datetime import date
data = int(input('Qual o ano de seu nascimento? '))
nao = (date.today().year - data) - 18
idade = date.today().year - data
tempo = idade - 18
falta = idade - date.today().year + data + (tempo * (-1))
print('Você completa {} anos nesse ano!'.format(idade))
if nao == 1:
    print('Seu alistamento militar foi no ano passado!')
elif nao == 0:
    print('Este é o ano do seu alistamento! Tenha seus documentos em mãos.')
elif tempo >= 1:
    print('Já se passaram {} anos do ano de seu alistamento militar!\nVocê deveria ter se alistado em {}!'.format(tempo, date.today().year - tempo))
elif idade == 17:
    print('Seu alistamento será no próximo ano, se prepare!')
elif tempo <= (-2):
    print('Você ainda não completou 18 anos, faltam {} anos para seu alistamento militar!'.format(falta))
    print('Seu alistamento deverá ser feito em {}'.format(date.today().year + falta))
