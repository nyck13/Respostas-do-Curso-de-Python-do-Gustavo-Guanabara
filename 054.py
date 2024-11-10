from datetime import date, datetime

nMaiores = 0
nMenores = 0

for i in range(0, 7):
    ano = int(input('Informe a sua idade: '))
    idade = datetime.today().year - ano
    if idade < 18 and idade >= 0:
        nMenores = nMenores + 1
    elif idade >= 18:
        nMaiores = nMaiores + 1
    else:
        print('Resposta inválida, encerrando o programa!')
        exit()
print('Foram {} pessoas maiores de idade e {} pessoas menores de idaede'.format(nMaiores, nMenores))