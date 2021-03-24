from math import *
ângulo=float(input('Digite o ângulo que você deseja:')) #tan=tangente/sin=seno/cos=cosseno
seno=sin(radians(ângulo)) #seno,cosseno e tangente precisam ser convertidos em radianos.
cosseno=cos(radians(ângulo))
tangente=tan(radians(ângulo))
print('O seno do ângulo fica: {:.2f}.'.format(seno))
print('O cosseno do ângulo fica: {:.2f}.'.format(cosseno))
print('A tangente do ângulo fica: {:.2f}.'.format(tangente))

