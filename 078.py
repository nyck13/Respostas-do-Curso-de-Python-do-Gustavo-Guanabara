lista = [int(input('Informe o primeiro valor: ')),
         int(input('Informe o segundo valor: ')),
         int(input('Informe o terceiro valor: ')),
         int(input('Informe o quarto valor: ')),
         int(input('Informe o quinto valor: '))]

print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor digitado foi {min(lista)} na posição {lista.index(min(lista))}')