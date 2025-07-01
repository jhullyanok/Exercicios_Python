#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Informe a temperatura: °C'))
f = c * 9 / 5 + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))
