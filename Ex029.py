print('Bom dia! Tenha uma ótima viagem!')
print('=-='*20)
velocidade=float(input('Qual velocidade está percorrendo?'))
print('=-='*20)
if velocidade > 80:
    print('AÍ NÃO, MERMÃO! Excedeu a velocidade de 80km/h.')
    multa=(velocidade - 80) * 7
    print('Sua multa tem o valor de R$ {:.2f}.'.format(multa))

else:
    print('PARABÉNS! PROSSIGA SUA VIAGEM!')