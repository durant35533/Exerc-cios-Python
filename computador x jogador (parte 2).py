from random import randint
computador = randint(0,10)
print('Sou seu computador...')
print('Vamos ver se você tem sorte!')
print('Advinhei o número entre 0 e 10. Será que acerta?')
tentativas = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    tentativas = tentativas + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais..')
        elif jogador > computador:
            print('Menos..')
print('Parabéns! Você acertou! Precisou de {} tentativas!'.format(tentativas))
print('Fim!')