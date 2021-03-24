sexo = str(input('Qual é o seu sexo? [M/F]')).strip().upper()[0]
while sexo not in 'MnFn':
    sexo=str(input('Tentativa inválida. Informe o seu sexo:')).strip().upper()[0]
print('O sexo {} foi registrado com sucesso!'.format(sexo))