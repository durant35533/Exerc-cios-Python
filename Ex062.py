primeiro = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a sua razão:'))
contador = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} > '.format(termo),end='')
        termo = termo + razão
        contador = contador + 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer utilizar?'))
print('FIM!')
print('O total de termos foi de {}.'.format(total))