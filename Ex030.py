número=int(input('Qual número você gostaria de colocar?'))
resultado= número % 2
if resultado == 0:
    print('O número {} é PAR!'.format(número))
else:
    print('O número {} é ÍMPAR.'.format(número))