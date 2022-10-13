import os
os.system('cls')

print('[0] - finalizar programa\n[1] - soma\n[2] - subtração\n[3] - divisão\n[4] - multiplicação\n[5] - exponenciação\n[6] - média aritimética\n[7] - média ponderada\n[8] - maior número digitado até o momento\n[9] - menor número digitado até o momento\n[10] - fatorial')
# setup
def soma():
    a = int(input('digite o 1 numero: '))
    b = int(input('digite o 2 numero: '))
    soma = a + b
    print(f'{a} + {b} = {soma}')
def sub():
    a = int(input('digite o 1 numero: '))
    b = int(input('digite o 2 numero: '))
    sub = a - b
    print(f'{a} - {b} = {sub}')
def div():
    a = int(input('digite o dividendo: '))
    b = int(input('digite o divisor: '))
    div = a / b
    print(f'{a} : {b} = {div}')
def mult():
    a = int(input('digite o 1 numero: '))
    b = int(input('digite o 2 numero: '))
    mult = a * b
    print(f'{a} x {b} = {mult}')
def expo():
    a = int(input('digite o numero: '))
    b = int(input('digite o expoente: '))
    expo = a ** b
    print(f'{a} ^ {b} = {expo}')
def medA():
    elem = int(input('digite a quantidade de elementos: '))
    a = 0
    somae = 0
    for elem in range (1, (elem+1)):
        a = int(input('digite um numero: '))
        somae += a
    medA = somae/elem
    print(f'{somae} / {elem} = {medA}')
def medP():
    elem = int(input('digite a quantidade de elementos: '))
    a = somae = somab = 0
    for elem in range (1, (elem+1)):
        a = int(input('digite um numero: '))
        b = int(input('digite o peso do mesmo: '))
        somae += a*b
        somab += b
    medP = somae/somab
    print(f'{somae} / {somab} = {medP}')
def fat():
    a = int(input('digite um numero: '))
    fat = 1
    for n in range(1,(a+1)):
        fat *= n
    print(f'{a}! = {fat}')

# console
while True:
    choice = int(input('digite operacao: '))
    if choice == 1:
        soma()
    if choice == 2:
        sub()
    if choice == 3:
        div()
    if choice == 4:
        mult()
    if choice == 5:
        expo()
    if choice == 6:
        medA()
    if choice == 7:
        medP()
    if choice == 10:
        fat()
