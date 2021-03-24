from math import factorial
número = int(input('Digite um número para fatorial:'))
c = número
print('Calculando {}!'.format(c))
f = 1
while c > 0:
    print('{}'.format(c),end=' ')
    print('x' if c > 1 else '=', end= ' ')
    f = f * c
    c = c - 1
print('{}'.format(f))