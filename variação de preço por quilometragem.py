km=float(input('Quantos quilômetros você percorreu?'))
if km <= 200:
    preço=km * 0.50
    print('O valor gasto foi de R$ {}.'.format(preço))
else:
    preço=km * 0.45
    print('Seu preço foi de R$ {}.'.format(preço))