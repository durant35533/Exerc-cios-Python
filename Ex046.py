from time import sleep
print('{:=^60}'.format('CONTAGEM REGRESSIVA DE FOGOS!'))
for c in range(10,-1,-1):
    sleep(1)
    print(c)
print('FOGOS SOLTADOS!! VIVA!!')