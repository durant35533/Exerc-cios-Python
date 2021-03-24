valor=float(input('Qual é valor da casa?'))
salário=float(input('Qual é o seu salário? R$'))
duração=int(input('Em quantos anos você vai pagar a casa que tu compras?'))
prestação=valor/(12*duração)
if prestação <= 0.30 * salário:
    print('Com base no valor R$ {:.2f}, o empréstimo PROCEDE!'.format(prestação))
else:
    print('Diante da aplicação do valor R$ {:.2f},o empréstimo NÃO PROCEDE!.'.format(prestação))
print('Até mais! Tenha um bom dia!')