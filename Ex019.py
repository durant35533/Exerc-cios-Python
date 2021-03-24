from random import *                    #"random" = "randonizador de elementos."
n1=input('Digite um nome:')         #choice é para escolhas aleatórias.
n2=input('Digite outro nome:')      #lista entre cochetes.
n3=input('Digite o terceiro nome:')
n4=input('Digite o quarto nome:')
lista=[n1,n2,n3,n4]
escolhido=choice(lista)
print('A pessoa que vai lavar os pratos hoje se chama: {}'.format(escolhido))
