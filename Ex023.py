número=int(input('Digite um número:'))
u=número//1 % 10
d=número//10 % 10
c=número//100 % 10
m=número//1000 % 10
print('Sua unidade é: {}'.format(u))
print('Sua dezena é: {}'.format(d))
print('Sua centena é: {}'.format(c))
print('Sua unidade de milhar é: {}'.format(m))




