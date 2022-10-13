import random
import time
import os
import winsound

#limpar tela


def clean():
    os.system('cls')


#input
clean()
ir = input("digite sim para começar: ")
#escolher aleatório (100%)
if ir == str('sim'):
    r = random.randint(1, 101)
    print('carregando..')
    time.sleep(1)
    clean()
else:
    print('oh..')

#SETUP
#matérias


def portugues():  # 20%
    print('português!!')
    time.sleep(0.6)
    Mpt = ['semântica e figuras', 'classificações', 'classificações',
'orações', 'concordância', 'concordância']
    print(f'a matéria escolhida foi: {random.choice(Mpt)}')


def matematica():  # 30%
    print('matemática!!')
    time.sleep(0.6)
    Mmat = ['conjunto', 'números', 'cálculo algébrico', 'cálculo algébrico',
            'equações', 'geometria', 'geometria', ]
    print(f'a matéria escolhida foi: {random.choice(Mmat)}')


def ciencias():  # 15%
    print('ciências!!')
    time.sleep(0.6)
    Mcien = ['ecologia', 'ecologia', 'zoologia', 'botânica', 'física', 'física',
'química', 'química']
    print(f'a matéria escolhida foi: {random.choice(Mcien)}')


def historia():  # 15%
    print('história!!')
    time.sleep(0.6)
    Mhist = ['antiguidade clássica', 'idade média', 'idade média', 'idade moderna',
'idade moderna', 'mundo contemporâneo', 'história do Brasil',
'história do Brasil']
    print(f'a matéria escolhida foi: {random.choice(Mhist)}')


def redacao():  # 20%
    print('redação!!')


#if's
if r >= 1 and r <= 20:
    portugues()
elif r > 20 and r <= 50:
    matematica()
elif r > 50 and r <= 65:
    ciencias()
elif r > 65 and r <= 80:
    historia()
elif r > 80 and r <= 100:
    redacao()
else:
    print(f"erro, o número é {r}.")

#POMODORO


def countdown(t):

    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    if t == 0:
        print('00:00')
        winsound.Beep(2500, 1000)

def pomodoro():
    tempo = int(input('quanto tempo (em minutos?): ')) * 60
    for i in range(3):
        print('\n\nestude!')
        countdown(tempo)
        print('\n\nlanchinho!!')
        countdown(10*60)

#display
time.sleep(0.5)
print('bons estudos!! ^^')
time.sleep(0.5)
input('aperte qualquer tecla para começar o pomodoro/cronometragem: ')
pomodoro()
#add pause e escrever materia