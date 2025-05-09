#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
m = float(input('Digite o metro desejado: '))
print('O metro {} convertido é:\nEm centimetros é {:.0f}cm!\nEm milímetros é {:.0f}mm!\nEm quilômetro  é {}km!\nEm hectometro é {}hm\nEm decametros é {}dam!\nEm decimetros é {}dm!'.format(m , m*100 , m *1000, m/1000, m/100, m/10, m*10))