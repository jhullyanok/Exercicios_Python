#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
a = int(input('Digite qualquer número: '))
print('O dobro de {} é {}!'.format(a, a*2))
print('O triplo de {} é {}!'.format(a, a*3))
print('A raiz quadrada de {} vale {:.3f}!'.format(a, a**(1/2)))
