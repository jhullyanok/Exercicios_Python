#Crie um programa que leia o nome de uma cidade e 
# diga se ela começa ou não com o nome “SANTO”.
cid = str(input('Digite o nome da cidade que voçê nasceu: ')).strip()
print(cid[0:5].capitalize() == 'Santo')
