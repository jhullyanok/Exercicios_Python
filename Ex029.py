#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual a velocidade atual do carro:Km '))
if velocidade > 80:
    multa = (velocidade - 80) *7
    print('MULTADO! Voçê execedeu o limite de velocidade que é de 80km/h.')
    print('O valor da multa é de {:.2f}R$.'.format(multa))
print('Tenha um bom dia!Dirija com segurança!')
