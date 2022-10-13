import os
os.system('cls')

n = int(input('digite um numero para converter:'))
e = int(input('digite\n[1] para binário\n[2] para octal\n[3] para hexadecimal\n'))

if e == 1:
  print(f'convertido para número binário: {format(n, "b")}') 
if e == 2:
  print(f'convertido para octal: {format(n, "o")}')
if e == 3:
  print(f'convertido para hexadecimal: {format(n, "x")}')