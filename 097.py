def escreva(frase):
    print('~'*len(frase))
    print(f'{frase}')
    print('~'*len(frase))

frase = str(input('Qual a sua mensagem? '))
escreva(frase)