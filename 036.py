valorCasa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você pretende pagar? '))

if valorCasa/(anos*12) <= 0.3*salario:
    print('Emprestimo aprovado!')
else:
    print('Empréstimo recusado!')