print('{:=^60}'.format('LOJA DO LULU!'))
dinheiro=float(input('Qual o valor a ser pago por esse produto? R$'))
print('''FORMAS DE PAGAMENTO:
[1] À vista dinheiro/cheque:10% de desconto.
[2] À vista no cartão:5% de desconto.
[3] Em até 2x no cartão: preço formal.
[4] 3x ou mais no cartão:20% de juros.''')
pagamento = int(input('Qual a sua forma de pagamento?'))
if pagamento == 1:
    preço = dinheiro * 0.90
    print('Optando pela primeira escolha, o preço a ser pago à vista é R$ {:.2f}.'.format(preço))
elif pagamento == 2:
    preço = dinheiro * 0.95
    print('Optando pela segunda escolha, o preço sendo à vista pelo cartão fica R$ {:.2f}.'.format(preço))
elif pagamento == 3:
    parcela = dinheiro/2
    print('Optando pela terceira escolha, as parcelas pagas em 2x no cartão fica em torno de R$ {:.2f}.'.format(parcela))
elif pagamento == 4:
    preço = dinheiro * 1.20
    parcelas = int(input('Quantas parcelas?'))
    total = preço/parcelas
    print('Com base nisso, o valor pago por parcela fica R$ {:.2f}.'.format(total))
    print('O novo preço, que custava R$ {:.2f}, com os juros passa a custar R$ {:.2f}.'.format(dinheiro,preço))
else:
    print('Tentativa inválida. Escolha uma das opções dadas, caro cliente.')