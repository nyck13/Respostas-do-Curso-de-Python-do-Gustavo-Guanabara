lista = list()
listaMulheres = list()
listaAcimaMedia = list()
qntdPessoas = media = soma = 0

while True:
    pessoa = {
        'nome': str(input('Informe o nome: ')).strip()
    }

    while True:
        sexo = str(input('Informe o sexo: [M]/[F] ')).strip().upper()
        if sexo in 'MF':
            pessoa['sexo'] = sexo
            if sexo == 'F':
                listaMulheres.append(pessoa['nome'])
            break
        else:
            print('O valor inserido não é válido, informe M ou F!')

    pessoa['idade'] = int(input('Informe a idade: '))
    lista.append(pessoa)
    qntdPessoas += 1

    resposta = str(input('Deseja continuar? [S]/[N]')).strip().upper()
    if resposta == 'N':
        break

for i in range(0, len(lista)):
    soma += lista[i]['idade']
media = soma/len(lista)

for i in range(0, len(lista)):
    if lista[i]['idade'] > media:
        listaAcimaMedia.append(lista[i]['nome'])

print('------------------------------')
print(f'A quantidade de pessoas cadastradas é de {qntdPessoas}')
print(f'A média de idade das pessoas da lista é de {media}')
print('As mulheres cadastradas foram ', end='')
for i in range(0, len(listaMulheres)):
    print(f'{listaMulheres[i]}', end=' ')
print()
print('As pessoas acima da média foram ', end='')
for i in range(0, len(listaAcimaMedia)):
    print(f'{listaAcimaMedia[i]}', end=' ')
