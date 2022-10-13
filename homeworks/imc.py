import os
os.system('cls')

kg = float(input('peso: '))
a = float(input('altura: '))
imc = kg/(a ** 2)
if imc < 18.5:
    print(f'IMC de {imc}, ABAIXO DO PESO.')
if imc > 18.5 and imc < 25:
    print(f'PESO IDEAL! IMC de {imc}')
if imc > 25 and imc < 30:
    print(f'IMC de {imc}, SOBREPESO.')
if imc > 30 and imc < 40:
    print(f'IMC de {imc}, OBESIDADE.')
if imc > 40:
    print(f'IMC de {imc}, OBESIDADE MÓRBIDA.')
    
