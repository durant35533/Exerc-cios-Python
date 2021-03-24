primeiro = int(input('Digite o primeiro termo:'))
razão = int(input('Digite sua razão:'))
termo = primeiro
c=1
while c <= 10:
    print('{} > '.format(termo),end='')
    termo = termo + razão
    c = c + 1
print('Fim do programa!')