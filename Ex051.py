print('{:=^60}'.format('PROGRESSÃO ARITMÉTICA!'))
primeiro = int(input('Digite um número:'))
razão = int(input('Qual a razão?'))
décimo = primeiro + (10-1) * razão
for c in range(primeiro,décimo,razão):
    print('{}'.format(c), end=' > ')
print('Acabou!')