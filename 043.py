peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso/(altura**2)

if imc < 18.5:
    print('Com {}kg e {} metros, você possui um IMC de {:.2f} e é classificado como ABAIXO DO PESO'.format(peso, altura, imc))
elif imc >= 18.5 and imc < 25.0:
    print('Com {}kg e {} metros, você possui um IMC de {:.2f} e é classificado como PESO IDEAL'.format(peso, altura, imc))
elif imc >= 25.0 and imc < 30.0:
    print('Com {}kg e {} metros, você possui um IMC de {:.2f} e é classificado como SOBREPESO'.format(peso, altura, imc))
elif imc >= 30.0 and imc < 40.0:
    print('Com {}kg e {} metros, você possui um IMC de {:.2f} e é classificado como OBESIDADE'.format(peso, altura, imc))
else:
    print('Com {}kg e {} metros, você possui um IMC de {:.2f} e é classificado como OBESIDADE MÓRBIDA'.format(peso, altura, imc))