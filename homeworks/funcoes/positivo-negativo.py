'''
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere P, 
se seu argumento for positivo, e N, se seu argumento for zero ou negativo.
'''
import os
os.system('cls')

def pn(n):
    if n > 0:
        return 'p'
    if n <= 0:
        return 'n'
i = float(input('digite um numero: '))
print(pn(i))

