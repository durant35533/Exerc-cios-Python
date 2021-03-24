import random   #random é para probabilidade
n1=input('Digite um nome:')       #shurffle é para colocar em ordem.
n2=input('Digite outro nome:')
n3=input('Digite o terceiro nome:')
n4=input('Digite o quarto nome:')
escolha=[n1,n2,n3,n4]
random.shuffle(escolha)
print('A ordem de quem deve lavar os pratos é: {}'.format(escolha))
