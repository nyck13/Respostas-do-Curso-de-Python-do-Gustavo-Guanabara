lista = list()

while True:
    nome = str(input('Informe o nome: ')).strip()
    n1 = float(input('Informe a primeira nota: '))
    n2 = float(input('Informe a segunda nota: '))

    aluno = [nome, n1, n2, (n1+n2)/2]
    lista.append(aluno)
    resposta = str(input('Deseja continuar? [S]/[N] ')).strip()
    if resposta in 'Nn':
        break

print('===== BOLETIM DO ALUNO =====')
print('No. Nome              Media ')
print('----------------------------')

for i in range(0, len(lista)):
    print(f'{i+1:<4}{lista[i][0]:<18}{lista[i][3]:<6}')

print('----------------------------')

while True:
    n = int(input('Deseja ver as notas de qual aluno? (999 INTERROMPE) '))
    if n != 999:
        print(f'As notas de {lista[n-1][0]} são: {lista[n-1][1]:.1f} {lista[n-1][2]:.1f}')
    else:
        break