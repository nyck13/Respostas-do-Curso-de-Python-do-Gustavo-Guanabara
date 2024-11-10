from time import sleep
from lib import interface
from lib import arquivo

arq = 'cursoemvideo.txt'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = interface.menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    match resposta:
        case 1:
            arquivo.lerArquivo(arq)
        case 2:
            interface.cabecalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = int(input('Idade: '))
            arquivo.cadastrar(arq, nome, idade)
        case 3:
            print('Saindo do sistema... Até mais!')
            break
        case _:
            print('\033[31mERRO! Informe uma opção válida\033[m')
    sleep(2)