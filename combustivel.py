#!/bin/python
# By: <stringuetta@gmail.com>

# Calculadora entre etanol x gasolina
import os
if os.name == 'nt':
    os.system('cls') or None
else:
    os.system('clear') or None
# Variaveis
print ('\033[0;31mCalculadora Etanol x Gasolina\033[m')
gasolina = float(input('Digita o valor da gasolina em R$: '))
etanol = float(input('Digita o valor do etanol em R$: '))
divisao = etanol / gasolina

if divisao > 0.70:
    print ('Em virtude do valor do Etanol está acima de 0.70 da gasolina, melhor escolha é colocar \033[0;33mGasolina\033[m')
else:
    print ('Em virtude do valor do Etanol está abaixo de 0.70 da gasolina, melhor escolha é \033[0;33mEtanol\033[m')

