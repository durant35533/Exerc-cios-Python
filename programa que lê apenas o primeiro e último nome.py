n=str(input('Digite o seu nome:')).strip()
nome=n.split()
print('Qual é o primeiro nome? {}'.format(nome[0]))
print('Qual é o seu último nome? {}'.format(nome[len(nome)-1]))
