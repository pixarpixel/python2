'''
Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres + , − e | . 
Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor 
mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados 
para valores dentro da faixa de forma elegante.
'''
import os
os.system('cls')

def linhas(l):
    if 0 < l < 21:
        print('+',end='')
        print('-'*l,end='')
        print('+')

def moldura(c: int, l: int):
    linhas(l)
    if 0 < c < 21:
        for i in range(1,c+1):
            print('|', end='')
            print(' '*l,end='')
            print('|')
    linhas(l)

l = int(input('digite o comprimento da largura: '))
c = int(input('digite o comprimento da altura: '))
moldura(c, l)