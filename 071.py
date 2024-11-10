print('=========================')
print('     BANCO NYELTIANO     ')
print('=========================')

valor = int(input('Qual valor você deseja sacar? '))
total = valor
cedula = 50
totalCedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print('Total de {} cédulas de R${}'.format(totalCedula, cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break