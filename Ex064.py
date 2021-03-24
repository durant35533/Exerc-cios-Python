número = 0
contador = -1
soma = -999
while número != 999:
    número = int(input('Digite um número:[999 para acabar.]'))
    soma = soma + número
    contador = contador + 1
print('FIM!')
print('{} números foram digitados.'.format(contador))
print('A soma dos números fica {}.'.format(soma))