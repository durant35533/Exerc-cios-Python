km=float(input('Quantos quilômetros o seu carro já rodou?'))
dias=float(input('Quantos dias você ficou com o carro?'))
preço=(60*dias) + (0.15*km)
print('Com base nisso, o preço gasto pelo uso do carro durante esse tempo foi de R${:.2f}.'.format(preço))

