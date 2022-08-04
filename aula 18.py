galera = list()
dados = list()
tmais = tmenos = 0
p1 = 0
for c in range(0, 3):
    p1 += 1
    dados.append(str(input(f'Nome da {p1} pessoa: ')))
    dados.append(int(input(f'Idade da {p1} pessoa ')))
    dados.append(str(input(f'Sxo da {p1} pessoa: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} tem {p[1]} anos, portanto, é de maior!')
        tmais += 1
    else:
        print(f'{p[0]} tem {p[1]} anos, portanto é de menor!')
        tmenos += 1
print(f'Temos {tmais} pessoas maior de idade e {tmenos} menor de idade.')