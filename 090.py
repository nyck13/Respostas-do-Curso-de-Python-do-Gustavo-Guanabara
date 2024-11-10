aluno = {'nome':str(input('Informe o nome: ')).strip(),
         'media':float(input("Informe a média: "))}
print('-'*25)
print(f'O nome é igual à {aluno['nome']}')
print(f'A média é igual à {aluno['media']}')
if aluno['media'] >= 7:
    print('A situação final é aprovado!')
elif 5 <= aluno['media'] <= 7:
    print('A situação final é recuperação!')
else:
    print('A situação final é reprovado!')