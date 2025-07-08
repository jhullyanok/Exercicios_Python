#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número qualquer: '))
if num %2 ==0:
    print('o número {} é PAR'.format(num))
else:
    print('o número {} é ÍMPAR'.format(num))