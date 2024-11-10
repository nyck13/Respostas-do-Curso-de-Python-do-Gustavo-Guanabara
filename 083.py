expressao = str(input('Informe a sua expressão: '))
pilha = list()

for simb in expressao:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simb)
            break

if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
