nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2)/2

if media >= 7:
    print('Sua média final é de {:.1f} e sua situação final é APROVADA'.format(media))
elif media >= 5 and media < 7:
    print('Sua média final é de {:.1f} e sua situação final é RECUPERAÇÃO'.format(media))
else:
    print('Sua média final é de {:.1f} e sua situação final é REPROVADA'.format(media))