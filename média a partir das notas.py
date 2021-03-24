n1=float(input('Digite a sua primeira nota:'))
n2=float(input('Digite a sua segunda nota:'))
média=(n1+n2)/2
if média < 5:
    print('Você está REPROVADOXINHO, CARAMBA!')
elif 7 > média >=5:
    print('Você está em RECUPERAÇÃOXINHA!')
elif média >=7:
    print('Você PAXOUXINHO! PARABÉNSXINHO!')
print('A sua média ficou: {}.'.format(média))
print('Tenha um ótimo dia!')