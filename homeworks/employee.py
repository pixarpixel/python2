import os 
os.system('cls')

nf = input('número do funcionário ou nome: ')
qtd = float(input('horas trabalhadas: '))
sh = float(input('salário por hora: '))
sal = sh*qtd
print(f'o(a) funcionário {nf} trabalhou {qtd} horas e recebeu {sal:.2f}')
