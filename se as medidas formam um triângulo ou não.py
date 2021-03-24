print('=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('=-' * 20)
seg1 = float(input('Primeiro segmento:'))
seg2 = float(input('Segundo segmento:'))
seg3 = float(input('Terceiro segmento:'))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos formam um triângulo!')
else:
    print('Os segmentos NÃO FORMAM um triângulo!')