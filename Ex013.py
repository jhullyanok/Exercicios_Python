#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print ('O funcionário que recebia R%{:.2f},com 15% de aumento,passará a receber R%{:.2f}!'.format(salario, aumento))
