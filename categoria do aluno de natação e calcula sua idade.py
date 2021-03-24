from datetime import *
from time import *
atual = date.today().year
nascimento = int(input('Olá, boa tarde! Qual a data do seu nascimento?'))
idade = atual - nascimento
print('Com base nisso..')
sleep(4)
if idade <=9:
    print('Sua categoria é MIRIM.')
elif idade > 9 and idade <=14:
    print('Sua categoria é INFANTIL.')
elif idade > 14 and idade <=19:
    print('Sua categoria é JÚNIOR.')
elif idade > 19 and idade <=25:
    print('Sua categoria é SÊNIOR.')
elif idade > 25:
    print('Sua categoria é MASTER.')
print('Sua classificação é essa, pois sua idade é de {} anos.'.format(idade))