print('{:=^60}'.format('CÁLCULO DE UM GRUPO DE PESSOAS!'))
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
mulhermenorde20 = 0
for pessoas in range(1,5):
    print('----{}ª PESSOA----'.format(pessoas))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo: [M/F]:')).strip()
    somaidade = somaidade + idade
    if pessoas == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhermenorde20 = mulhermenorde20 + 1
médiaidade = somaidade/4
print('=' * 80)
print('A média desse grupo referido é de {:.2f} anos.'.format(médiaidade))
print('=' * 80)
print('O homem mais velho se chama {} e ele tem {} anos de idade.'.format(nomevelho,maioridadehomem))
print('=' * 80)
print('Existem {} mulheres que têm menos de 20 anos.'.format(mulhermenorde20))