#Escreva um programa que pergunte o salário de um funcionário e 
# calcule o valor do seu aumento. Para salários superiores a R$1250,00, 
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250.00:
    print('O aumento no salário é de 10% e ele passará a receber R${:.2f}.'.format((salario * 10 / 100)+salario))
else:
    print('O aumento no salário é de 15% e ele passará a receber R${:.2f}.'.format((salario * 15 / 100)+salario))
