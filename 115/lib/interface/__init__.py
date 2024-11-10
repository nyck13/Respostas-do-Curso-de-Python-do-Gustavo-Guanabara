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

def linha(tam = 42):
    print('-' * tam)

def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[34m{item}\033[m')
        contador += 1
    linha()
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
