import os
os.system('cls')

c = int(input('valor do capital inicial: '))
t = int(input('tempo (em meses) que o dinheiro ficará investido: ')) /100
i = int(input('taxa de juros aplicada: '))
j = c*i*t
tot = j + c
print(f'o total de juros é: {j}\no valor total do capital após os meses é: {tot}')