#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
m = float(input('Digite o metro desejado: '))
print('O metro {} convertido é: '.format(m))
print('Em centimetros é {:.0f}cm! '.format(m *100))
print('Em milímetros é {:.0f}mm! '.format(m *1000))
print('Em quilômetro  é {}km! '.format(m /1000))
print('Em hectometro é {}hm! '.format(m /100))
print('Em decametros é {}dam! '.format(m /10))
print('Em decimetros é {}dm! '.format(m *10))
