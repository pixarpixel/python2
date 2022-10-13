'''
Criar um programa que simule um Bingo, você deverá programar duas cartelas com 6 números para você usuário 
jogar e outra o computador. E a cada rodada o programa deve lhe apresentar um número aleatório dentro de 
1 à 60. Ao completar a sua cartela apresente uma mensagem tipo: 'BINGO!!! e quem ganhou'. 
A quantidade de rodadas e quais números a cartela perdedora faltou completar.
ps: não precisa usar random
'''
import time
import os 
os.system("cls")

jogador = set()
computador = set()
bingo1 = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60'}
bingo = set()

for n in range(1, 61):
    bingo.add(str(n))
    jogador.add(str(n))
for i in range(1, 7): 
    computador.add(bingo.pop())
for i in range(1, 55):
    jogador.pop()

print('BINGO',20*'=','\nSua cartela: ',jogador)
time.sleep(1)
while True:
    num = bingo1.pop()
    print(f'número escolhido: {num}')
    time.sleep(1)    
    if num in jogador:
        print(f'sua cartela: {jogador}')
    jogador.discard(num)
    time.sleep(1)
    computador.discard(num)
    if len(computador) <= 0:
        print("COMPUTADOR GANHOU!!")
        print(f"você perdeu :( números que faltavam: {jogador}")
        break
    if len(jogador) <= 0:
        print("JOGADOR GANHOU!!")
        print(f"computador perdeu :( números que faltavam: {computador}")
        break



