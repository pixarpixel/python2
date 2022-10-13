import os 
os.system('cls')

per = ["Telefonou para a vítima?",
"Esteve no local do crime?",
"Mora perto da vítima?",
"Devia para a vítima?",
"Já trabalhou com a vítima?"]
s = 0
for item in per:
    print(item)
    r = input('s/n?\n').lower()
    os.system('cls')
    if r == 's':
        s += 1 
if s == 2: 
    print('Suspeito')
if s == 3 or s == 4:
    print('Cúmplice')
if s == 5:
    print('Culpado')
else:
    print('Inocente')


