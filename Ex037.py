número=int(input('Digite um número inteiro:'))
print('''Escolha uma das bases de conversão:
[1] Conversão para BINÁRIO
[2] Conversão para OCTAL
[3] Conversão para HEXADECIMAL''')
opção = int(input('Diga a opção:'))
if opção == 1:
    print('O número {} convertido para Binário fica: {}.'.format(número,bin(número)))
elif opção == 2:
    print('O número {} convertido em OCTAL fica: {}.'.format(número,oct(número)))
elif opção == 3:
    print('O número {} convertido em HEXADECIMAL fica: {}.'.format(número,hex(número)))
else:
    print('Opção inválida. Tente novamente.')