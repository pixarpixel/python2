'''
5) Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e 
custo, que é o custo de um item antes do imposto. 
A função “altera” o valor de custo para incluir o imposto sobre vendas.
'''
import os
os.system('cls')

def somaImposto(custo, taxaImposto):
    custo = custo + (custo*taxaImposto/100)
    return custo  
c = int(input("digite o custo: "))
t = int(input("digite a taxa do imposto: "))
print(f"O total é: R${somaImposto(c, t)}" )