qntdMais18 = 0
mulheresMenor20 = 0
qntdHomens = 0

while True:
    print('-------------------------')
    print('   CADASTRE UMA PESSOA   ')
    print('-------------------------')

    idade = int(input('Idade: '))
    while idade < 0:
        print('Informe o valor correto para a idade! ')
        idade = int(input('Idade: '))

    sexo = str(input('Sexo: [M]/[F]: ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        print('Informe o valor correto para o sexo! ')
        sexo = str(input('Sexo: [M]/[F]: ')).strip().upper()

    if idade > 18:
        qntdMais18 += 1
    if sexo == 'M':
        qntdHomens +=1
    elif sexo == 'F':
        if idade < 20:
            mulheresMenor20 += 1

    resposta = str(input('Deseja continuar? [S]/[N] ')).strip().upper()
    while resposta != 'S' and resposta != 'N':
        print('Informe uma resposta válida! ')
        resposta = str(input('Deseja continuar? [S]/[N] ')).strip().upper()
    if resposta == 'N':
        break

print('''A quantidade de pessoas com mais de 18 anos é {}
A quantidade de homens cadastrados é {}
A quantidade de mulheres cadastradas que possuem menos de 20 anos é {}'''.format(qntdMais18, qntdHomens, mulheresMenor20))
