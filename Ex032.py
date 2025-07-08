# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from calendar import isleap
from datetime import date
ano = int(input('Qual ano deseja analizar? Digite 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if isleap(ano):
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não bissexto!'.format(ano))
