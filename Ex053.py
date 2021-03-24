frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1,-1,-1):
    inverso += junto[letra]
print('O inverso de {} fica {}.'.format(junto,inverso))
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Essa frase NÃO É UM PALÍNDROMO!')