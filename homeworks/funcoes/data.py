''''
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e 
devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL 
caso a data seja inválida.
'''
import os
os.system('cls')

def data(d,m,a):
    meses  = {1: 'janeiro',2: 'fevereiro',3: 'março',4: 'abril',5: 'maio',6: 'junho',7: 'julho',
        8: 'agosto',9: 'setembro',10: 'outubro',11: 'novembro',12: 'dezembro'}
    if 0 < int(m) < 13  and 0 < int(d) < 32:
        return f'{d} de {meses[int(m)]} de {a}'
    else: 
        return 'NULL'

date = input('escreva a data em formato dd/mm/aaaa: ')
d, m, a = date.split('/')
print(data(d,m,a))

