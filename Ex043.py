from time import *
print('Olá, bom dia!')
peso=float(input('Qual é o seu peso em KG?'))
altura=float(input('Qual é a sua altura em metros?'))
print('Aguardando o seu resultado...')
sleep(4)
IMC = peso/(altura)**2
if IMC < 18.5:
    print('Status: ABAIXO DO PESO.')
elif IMC >= 18.5 and IMC < 25:
    print('Status: PESO IDEAL.')
elif IMC >= 25 and IMC < 30:
    print('Status: SOBREPESO')
elif IMC >=30 and IMC < 40:
    print('Status: OBESIDADE.')
elif IMC >= 40:
    print('Status: OBESIDADE MÓRBIDA.')
else:
    print('Tentativa inválida. Tente mais uma vez, caro cliente.')
print('Seu resultado é esse, pois o seu IMC vale {:.2f}.'.format(IMC))