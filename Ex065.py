resposta = 'S'
contador = 0
soma = 0
maior = 0
menor = 0
while resposta in 'Ss':
    número=int(input('Digite um número inteiro:'))
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    contador = contador + 1
    soma = soma + número
    média = soma/contador
    if contador == 1:
        maior = número
        menor = número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número
print('A média desse grupo de {} números é de {}'.format(contador,média))
print('O maior número citado na lista é {} e o menor vale {}.'.format(maior,menor))
print('ACABOU!')