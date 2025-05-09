#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
carteira = float(input('Valor na carteira:'))
print('Com {} reais na sua carteira,voçê pode comprar {:.2f} dolares!'.format(carteira, carteira*5.71))
