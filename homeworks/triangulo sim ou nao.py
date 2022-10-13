import os
os.system('cls')

a = float(input('lado 1 do suposto triângulo: '))
b = float(input('lado 2: '))
c = float(input('lado 3: '))

if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print('este triangulo nao existe.')
else:
   print('este triangulo existe.') 