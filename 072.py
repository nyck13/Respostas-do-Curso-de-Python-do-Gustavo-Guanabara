extenso = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
while True:
    n = int(input('Informe um número de 0 até 20: '))
    if n >= 0 and n <= 20:
        break;
    print('Informe um número válido!')
print(f'O seu número é {extenso[n]}')