from random import randint
número = randint(1,6)
print('-=-'*20)
print('Vou pensar em um número que fique entre 1 e 6. Tente adivinhar..')#faz o computador "PENSAR"
print('-=-'*20)
jogador=int(input('Qual o número que pensei?'))
print('-=-'*20)
if jogador == número:
    print('PARABÉNS! VOCÊ ACERTOU!')
else:
    print('ERROU! VOCÊ ESTÁ COM FALTA DE SORTE.')
print('Eu pensei no número: {}'.format(número))