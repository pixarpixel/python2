import os
import random
import time
os.system('cls')

ppt = ['pedra', 'papel', 'tesoura']
computador = random.choice(ppt)
jogador = input('pedra, papel, ou tesoura?: ')

if computador == 'pedra' and jogador == 'tesoura' or computador == 'papel' and jogador == 'pedra' or computador == 'tesoura' and jogador == 'papel':
   print('PEDRA... PAPEL... TESOOOURA!')
   time.sleep(1)
   print(f'computador ganhou! ele jogou {computador}')

if jogador == 'pedra' and computador == 'tesoura' or jogador == 'papel' and computador == 'pedra' or jogador == 'tesoura' and computador == 'papel':
    print('PEDRA... PAPEL... TESOOOURA!')
    time.sleep(1)
    print(f'jogador ganhou! o computador jogou {computador}!')

