#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Digite um número de 0 a 9999: '))
if 0 <=num <= 9999:
    print('Analizando o número {}...'.format(num))
    print('Unidade: {}'.format(num //1 %10))
    print('Dezena: {}'.format(num //10 %10))
    print('Centena: {}'.format(num //100 %10))
    print('Milhar: {}'.format(num //1000 %10))
else:
    print('Erro:O número deve estar entre 0 e 9999.')
