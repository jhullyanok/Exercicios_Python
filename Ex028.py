#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('\nBem Vindo ao jogo de adivinhação v.1.0\n')
print ('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
n = randint(0, 5)
a = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if a < 0 or a > 5:
    print('Erro: Digite um número entre 0 e 5.')
if a == n:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! Eu pensei no número {}.'.format(n))
print('\n---Obrigado por jogar---\n')
