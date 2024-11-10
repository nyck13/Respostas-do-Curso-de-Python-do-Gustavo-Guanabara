somaIdades = 0
idadeHomemVelho = 0
nomeHomemVelho = ""
mulheresAbaixo20 = 0

for i in range(0, 4):
    print('Pessoa de número {}'.format(i + 1))
    nome = str(input('Informe o nome: ')).strip()
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo [M]/[F]: ')).strip()
    somaIdades = somaIdades + idade

    if sexo == 'M' and idade > idadeHomemVelho:
        nomeHomemVelho = nome
        idadeHomemVelho = idade
    if sexo == 'F' and idade < 20:
        mulheresAbaixo20 = mulheresAbaixo20 + 1


media = somaIdades/4

print('''A média da idade das pessoas é de {:.2f} anos
O nome do homem mais velho é {}
A quantidade de mulheres com idade menor que 20 anos é {}'''.format(media, nomeHomemVelho, mulheresAbaixo20))
