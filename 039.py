from datetime import date

ano = int(input('Informe o ano do seu nascimento: '))
anoAlistamento = ano + 18
idade = date.today().year - ano

if idade == 18:
    print('Você nasceu em {} e tem 18 anos, você deve se alistar agora!'.format(ano))
elif idade > 18:
    print('Você nasceu em {} e tem {} anos, já deveria ter se alistado em {} e está {} anos atrasado'.format(ano, idade, anoAlistamento, idade - 18))
else:
    print('Você possui {} anos e não é obrigado a se alistar'.format(idade))