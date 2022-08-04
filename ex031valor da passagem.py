km = int(input('De quantos kilômetros será sua viajem? '))
if km <= 150:
    pr = km * 0.5
else:
    pr = km * 0.35
print('Preço: R${}'.format(pr))