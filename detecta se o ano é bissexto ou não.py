from datetime import date
ano=int(input('Qual o ano que você deseja colocar? Coloque 0 para ver o ano atual:'))
if ano == 0:
    ano=date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  #!= não é diferente
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO!'.format(ano))
