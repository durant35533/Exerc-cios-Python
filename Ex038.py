n1=float(input('Digite o primeiro número:'))
n2=float(input('Digite o segundo número:'))
if n1>n2:
    print('O número {} é maior do que {}!'.format(n1,n2))
elif n2>n1:
    print('O número {} é maior do que o número {}!'.format(n2,n1))
else:
    print('O dois são IGUAIS.')
