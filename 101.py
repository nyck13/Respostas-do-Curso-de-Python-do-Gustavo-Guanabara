from datetime import datetime

def voto(ano):
    idade = datetime.today().year - ano
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'

nascimento = int(input('Informe o ano do seu nascimento: '))
print(f'Você possui {datetime.today().year - nascimento} anos, o voto é {voto(nascimento)}')