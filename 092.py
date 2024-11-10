from datetime import datetime

pessoa = {
    'nome':str(input('Informe o nome: ')),
    'ano':int(input('Informe o ano de nascimento: ')),
    'carteira':int(input('Informe o número da carteira de trabalho: (0 se não possui) '))
}
pessoa['idade'] = datetime.today().year - pessoa['ano']
if pessoa['carteira'] != 0:
    pessoa['contratacao'] = int(input('Informe o ano de contratação: '))
    pessoa['salario'] = float(input('Informe o salário: '))
    pessoa['aposentadoria'] = (35 - (datetime.today().year - pessoa['contratacao'])) + pessoa['idade']

print('-----------------')

print(f'O nome da pessoa é {pessoa['nome']}')
print(f'Possui {pessoa['idade']} anos')
if pessoa['carteira'] != 0:
    print(f'O número da carteira de trabalho é {pessoa['carteira']}')
    print(f'A contratação tem o valor de {pessoa['contratacao']}')
    print(f'A pessoa ganha RS{pessoa['salario']:.2f}')
    print(f'Aposentadoria tem o valor de {pessoa['aposentadoria']}')