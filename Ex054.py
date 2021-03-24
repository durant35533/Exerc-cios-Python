from datetime import *
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1,8):
    nascimento = int(input('Qual o ano a {}ª pessoa nasceu?'.format(pessoas)))
    idade = atual - nascimento
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('Existem {} que são de menor e {} que são de maior de idade.'.format(totmenor,totmaior))