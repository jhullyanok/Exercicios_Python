#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
a = float(input('Nota 1 do aluno: '))
b = float(input ('Nota 2 do aluno: '))
s = (a+b) /2
print('A média entre {:.1f} e {:.1f} é {:.1f}!'.format(a, b, s))
