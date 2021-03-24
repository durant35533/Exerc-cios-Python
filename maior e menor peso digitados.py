print('{:=^60}'.format('CLASSIFICAÇÃO DOS PESOS!'))
maior = 0
menor = 0
for pessoas in range(1,6):
    peso=int(input('Digite o peso da {}ª pessoa:'.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
       if peso > maior:
           maior = peso
       elif peso < menor:
           menor = peso
print('O maior peso medido foi de {} KG.'.format(maior))
print('O menor peso medido foi de {} KG.'.format(menor))