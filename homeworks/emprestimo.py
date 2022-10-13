import os
os.system('cls')

c = float(input('valor da casa: '))
s = float(input('salário do comprador: '))
a  = float(input('em quantos anos irá pagar: '))
pay = c/(a*12)
if pay < s*(30/100):
    print(f'a prestação é de {pay} mensalmente.') 
else:
    print(f'sua prestação mensal deu {pay} e é menor que 30% do seu salário.')
