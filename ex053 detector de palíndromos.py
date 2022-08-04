frase = str(input('Escreva uma frase: ')).strip().upper()
pal = frase.split()
junto = ''.join(pal)
inv = (junto[::-1])
print(junto, inv)
if junto == inv:
    print('ESTA FRASE É PALÍNDOMA!')
else:
    print('ESTA FRASE NÃO É PALÍNDROMA!')
