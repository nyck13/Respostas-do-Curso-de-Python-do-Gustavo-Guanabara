import math

angulo = math.radians(float(input('Informe o valor do ângulo: ')))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('O valor do seno, do cosseno e da tangente do ângulo é, respectivamente, {:.2f}, {:.2f}, {:.2f}'.format(seno, cosseno, tangente))