def leiaInt(string):
    while True:
        try:
            n = int(input(f'{string}'))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: Digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[0;31mERRO: O usuário preferiu não informar o valor\033[m')
            return 0
        else:
            return n

def leiaFloat(string):
    while True:
        try:
            n = float(input(f'{string}'))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: Digite um número real válido\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[0;31mERRO: O usuário preferiu não informar o valor\033[m')
            return 0
        else:
            return n


nInt = leiaInt('Informe um número inteiro: ')
nFloat = leiaFloat('Informe um número de ponto flutuante: ')
print(f'Você acabou de digitar o número inteiro {nInt} e o número real {nFloat}')