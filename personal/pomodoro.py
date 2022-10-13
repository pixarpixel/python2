import time
import os
import winsound

os.system('cls')
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
        os.system('cls')
countdown(5)
countdown(5)
