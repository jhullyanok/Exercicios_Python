#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: ').strip())
print('Analizando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('O seu nome tem ao total {} letras'.format(len(nome.replace(' ', ''))))
print('E o seu primeiro nome tem {} letras ao total.'.format(len(nome.split()[0])))