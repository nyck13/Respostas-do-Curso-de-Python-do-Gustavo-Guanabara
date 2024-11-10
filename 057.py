sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o seu sexo [F]/[M]: ')).upper().strip()

if sexo == 'M':
    print('Você é do sexo masculino!')
else:
    print('Você é do sexo feminino!')