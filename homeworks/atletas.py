import os 
os.system('cls')

a = int(input('ano de nascimento: '))
idade = 2022-a

print(idade)

if idade <= 9:
    print('CATEGORIA MIRIM')
if idade > 9 and idade <= 14:
    print('CATEGORIA INFANTIL')
if idade > 14 and idade <= 23:
    print('CATEGORIA JUNIOR')
if idade > 23 and idade <= 30:
    print('CATEGORIA SENIOR')
if idade > 30:
    print('CATEGORIA MASTER')
    
