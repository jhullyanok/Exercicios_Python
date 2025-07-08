#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#E a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
rodados = float(input('Quantos Km foram percorridos:Km '))
dias = int(input('Por quantos dias ele foi alugado: '))
preço = (dias*60) + (rodados*0.15)
print('Com {}km rodados e {} dias alugados,voçê pagará R${:.2f} no aluguel do carro.'.format(rodados, dias, preço))