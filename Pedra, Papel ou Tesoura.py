from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura') # 0,1,2
computador = randint(0,2)
print('Vamos um Jokenpô? Vou te derrotar!')
print('''Faça uma escolha da jogada que você gostaria de fazer:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual a sua jogada?'))
print('JO')
sleep(2)
print('KEN')
sleep(2)
print('PÔ!!!')
print('Computador jogou {}.'.format(itens[computador]))
print('O jogador jogou {}.'.format(itens[jogador]))
if computador == 0: # computador jogou PEDRA.
    if jogador == 0:
        print('DUELO EMPATADO!')
    elif jogador == 1:
        print('O jogador VENCEU!')
    elif jogador == 2:
        print('O computador VENCEU!')
    else:
        print('Jogada inválida!')
elif computador == 1: # Computador jogou PAPEL.
    if jogador == 0:
        print('O computador VENCEU!')
    elif jogador == 1:
        print('Duelo EMPATADO!')
    elif jogador == 2:
        print('O jogador VENCEU!')
    else:
        print('Jogada inválida!')
elif computador == 2: #Computador jogou TESOURA.
    if jogador == 0:
        print('O jogador VENCEU!')
    elif jogador == 1:
        print('O computador VENCEU!')
    elif jogador == 2:
        print('Duelo empatado!')
    else:
        print('Jogada inválida!')
else:
    print('Jogada inválida. Tente de novo!')
