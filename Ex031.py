# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
# e R$0,45 parta viagens mais longas.
distancia = float(input('Qual foi a distância da viagem?Km '))
print('Voçê está preste a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    print('O valor da passagem é de R%{:.2f}.'.format(distancia*0.50))
else:
    print('O valor da passagem é de R%{:.2f}.'.format(distancia*0.45))
