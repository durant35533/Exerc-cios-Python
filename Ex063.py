print('{:~^60}'.format('SEQUÊNCIA DE FIBONACCI!'))
n = int(input('Quantos termos quer mostrar?'))
t1=0
t2=1
print('{} > {}'.format(t1,t2),end='')
contador = 3
while contador <= n:
    t3 = t1 + t2
    print(' > {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    contador = contador + 1
print(' > FIM!')