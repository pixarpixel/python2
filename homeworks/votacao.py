import os

#setup
os.system('cls')
tot = ca = di = ganhador = vic = vin = pe = 0
li = ['camila', 'diego', 'victor', 'vinicius', 'pedro']

# console
print('''Em quem você deseja votar: 
[Camila]
[Diego]
[Victor]
[Vinicius]
[Pedro]''')

while True:
    vot = input("").lower()
    os.system('cls')
    print('''Em quem você deseja votar: 
[Camila]
[Diego]
[Victor]
[Vinicius]
[Pedro]''')
    if vot in li:
      tot += 1 
      if vot == 'camila':
         ca += 1
      if vot == 'diego':
         di += 1 
      if vot == 'victor':
         vic += 1
      if vot == 'vinicius':
         vin += 1
      if vot == 'pedro':
         pe += 1
    elif vot == 'fim':
        break
    else: 
      print('voto em branco e/ou voto inválido. tente novamente.')

li2 = [ca, di, vic, vin, pe]
li2.sort()

print(f'''\n\ntotal de votos: {tot}
camila: {ca} = {(100*ca)/tot:.1f}%
diego: {di} = {(100*di)/tot:.1f}%
victor: {vic} = {(100*vic)/tot:.1f}%
vinicius: {vin} = {(100*vin)/tot:.1f}%
pedro: {pe} = {(100*pe)/tot:.1f}%
ganhador: {li2[-1]} com {(100*li2[-1])/tot:.1f}%''')

