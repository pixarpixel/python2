'''
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. 
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
Registre a informação A.M./P.M. como um valor A para A.M. e P para P.M. Assim, a função para efetuar 
as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita 
que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
'''
import os
os.system('cls')

def converterhora(hora: int, min: int):
    if 24 > hora > 12:
        hora -= 12
        convertido = f"{hora}:{min} PM"
    elif hora == 24:
        hora = 0
    elif  24 > hora < 12  : 
        convertido = f"{hora}:{min} AM"
    return convertido

while True:
    horario = input('horario a ser convertido: ')
    hora, min = horario.split(':')
    print(converterhora(int(hora), int(min)))
