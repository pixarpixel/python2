import math
import os
os.system('cls') #limpar

ca = int(input('comprimento do cateto adjacente: '))
co = int(input('comprimento do cateto oposto: '))
h = math.sqrt(ca**2 + co**2)
print(f'o comprimento da hipotenusa é: {h}')
