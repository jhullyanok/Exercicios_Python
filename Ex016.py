from math import trunc, floor, ceil
num = float(input("Digite um número: "))
print('\nO número {} tem a parte inteira {}\nO número arredondado para cima é {}\nO número arredondado para baixo é {}\n' .format(num, trunc(num), ceil(num), floor(num)))

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a parte inteira desse número.