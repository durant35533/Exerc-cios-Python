n1=float(input('O primeiro valor:'))
n2=float(input('O segundo valor:'))
n3=float(input('O terceiro valor:'))
#verificando quem é menor e é possível fazer quem é o maior pelo mesmo procedimento.
menor=n1
if n2 < n1 and n2 < n3:
    menor=n2
if n3 < n1 and n3 < n2:
    menor=n3
print('O menor valor digitado foi {}.'.format(menor))