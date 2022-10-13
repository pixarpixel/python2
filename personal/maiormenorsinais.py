import random


a = random.randint(1, 100)
maiormenor = ['>', '<']
num = [a, 'x']
num2 = [a, 'x']
conta = f'{random.choice(num)} {random.choice(maiormenor)} {random.choice(num)}'   
if maiormenor == '>':
    input('lal')
    print('maior')
elif maiormenor == '<':
    input('lal')
    print('menor')
if random.choice(num) == random.choice(num2):
    print(conta)
else:
    a = random.randint(1, 100)
    maiormenor = ['>', '<']
    num = [a, 'x']
    num2 = [a, 'x']
    conta = f'{random.choice(num)} {random.choice(maiormenor)} {random.choice(num)}'   
    if maiormenor == '>':
        input('lal')
        print('maior')
    elif maiormenor == '<':
        input('lal')
        print('menor')
    if random.choice(num) == random.choice(num2):
        print(conta)