from time import *
n1 = float(input('Digite um valor:'))
n2 = float(input('Digite outro valor:'))
escolha = 0
while escolha != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    escolha = int(input('Qual é a sua escolha?'))
    print('=' * 50)
    if escolha == 1:
        soma = n1 + n2
        print('A soma entre os valores é: {}'.format(soma))
        print('=' * 50)
    elif escolha == 2:
        mult = n1 * n2
        print('A multiplicação entre os valores vale: {}'.format(mult))
        print('=' * 50)
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número é {}.'.format(maior))
        print('=' * 50)
    elif escolha == 4:
        print('Informe novos números...')
        n1 = float(input('Digite um número:'))
        print('=' * 50)
        n2 = float(input('Digite outro número:'))
        print('=' * 50)
    elif escolha == 5:
        print('Finalizando...')
        sleep(2)
print('Fim do programa. Até breve!')