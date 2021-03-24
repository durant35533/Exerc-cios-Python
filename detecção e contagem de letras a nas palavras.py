frase=str(input('Digite uma frase:')).strip()
print('Quantas letras A existem na frase? {}'.format(frase.count('A')))
print('Onde vai aparecer a primeira letra a? {}'.format(frase.find('a')))
print('Qual a posição que vai aparecer o último a? {}'.format(frase.rfind('a')))