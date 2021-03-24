from datetime import *
atual=date.today().year
nascimento=int(input('Qual é o ano do seu nascimento?'))
idade = atual - nascimento
print('Você que nasceu em {} tem, hoje em dia, {} anos de idade em {}.'.format(nascimento,idade,atual))
if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade < 18:
    tempo = 18 - idade
    print('Você ainda é novo, mas falta(m) {} ano(s) para se alistar ao exército.')
elif idade > 18:
    tempo = idade - 18
    print('Já se passou/passaram {} ano(s) do seu alistamento militar.'.format(tempo))