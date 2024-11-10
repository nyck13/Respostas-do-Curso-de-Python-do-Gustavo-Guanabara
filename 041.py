from datetime import date

ano = int(input('Informe o ano do seu nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('Você possui {} anos e está na categoria MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você possui {} anos e está na categoria INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você possui {} anos e está na categoria JUNIOR'.format(idade))
elif idade > 19 and idade <= 25:
    print('Você possui {} anos e está na categoria SÊNIOR'.format(idade))
else:
    print('Você possui {} anos e está na categoria MASTER'.format(idade))