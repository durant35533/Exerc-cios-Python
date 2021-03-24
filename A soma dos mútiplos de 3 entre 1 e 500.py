contador = 0
soma = 0
print('A soma entre os múltiplos de 3 que está entre 1 e 500 vale:')
for c in range(1,501,2):
    if c % 3 ==0:
        print(c)
        soma = soma + c
        contador = contador + 1
print('A soma dos {} valores vale {}.'.format(contador,soma))