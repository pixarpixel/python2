'''
1) Faça um programa para imprimir:
1  {i * i}
2   2 {i * (i+1)}
3   3   3 {i *}
.....
n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
'''
import os
os.system('cls')

def numeros(n):
    count = 0
    for i in range (1, n+1):
        count += 1
        print((f"{i} " * count))

n = int(input('Digite um número: '))
numeros(n)

