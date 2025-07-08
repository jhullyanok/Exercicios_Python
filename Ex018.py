#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin,cos,tan,radians
angulo = float(input('Digite o valor do ângulo desejado: '))
conversao = radians(angulo)
print('\nSENO:{:.2f}\nCOSSENO:{:.2f}\nTANGENTE:{:.2f}\n'.format(sin(conversao),cos(conversao),tan(conversao)))
