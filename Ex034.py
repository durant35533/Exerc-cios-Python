salário=float(input('Qual é o seu salário?'))
if salário <= 1250:
    dinheiro=salário*1.15
    print('Com o aumento, o seu salário passa a ser de R${:.2f}.'.format(dinheiro))
else:
    dinheiro=salário*1.10
    print('Com o aumento, o seu salário fica em torno de R${:.2f}.'.format(dinheiro))