import os 
os.system('cls')

n1 = float(input('digite um numero: '))
n2 = float(input('digite outro numero: '))
if n1 < n2:
    print('o segundo é maior')
if n1 == n2:
    print('não há maior')
if n1 > n2:
    print('o primeiro é maior')