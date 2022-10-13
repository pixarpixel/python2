import os
os.system('cls')

v = int(input('Valor do saque: R$ ')) # valor
print('=' * 30)
for nota in [50, 20, 10, 5, 2, 1]:
    qtd = v // nota
    v = v % nota
    if qtd > 0:
        print(f'{qtd} nota(s) de R$ {nota}') 