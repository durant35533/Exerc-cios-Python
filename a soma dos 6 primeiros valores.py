soma = 0
for c in range(1,7):
    número = int(input('Digite um valor:'))
    if número % 2 == 0:
        soma = soma + número
print('A soma desses valores deu {}.'.format(soma))


