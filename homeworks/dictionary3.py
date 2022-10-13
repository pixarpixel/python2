a = dict() #dicionarios das notas
maiornota = dict() 
menornota = dict()
mediaano = dict()
resultado = dict()
al = soma = menor = maior = 0
no = [] #lista para ver maior menor 

while True:
    al = input('Aluno(a): ')    
    if al == 'fim':
        break
    a.update({al: []})
    menornota.update({al: []})
    maiornota.update({al: []})
    mediaano.update({al: []})

    for i in range (1, 5): #perguntar cada nota
        n = int(input(f'Nota {i}°: '))
        no.append(n) if n <= 10 else print('nota inválida.')
        a[al].append(n) 
    no.sort()
    maiornota[al].append(no[-1]) #pos da lista para maior/menor e media
    menornota[al].append(no[0])
    mediaano[al].append(sum(no)/len(no))
    if sum(no)/len(no) > 6: #aprovado/reprovado
        resultado.update({al: 'Aprovado'})
    elif sum(no)/len(no) == 6:
        resultado.update({al: 'Recuperação'})
    else:
        resultado.update({al: 'Reprovado'})
    no.clear()
# ver cada aluno
print('\n',30*'=')
acessar = input('qual aluno deseja ver?: ')
while acessar in a:
    r = int(input('''[1] Maior nota
[2] Menor nota
[3] Média do ano
[4] Todas as notas
[5] Resultado
[6] Encerra o programa
'''))
    if r == 1:
        print(f'maior nota: {maiornota[acessar]}') 
    elif r == 2:
        print(f'menor nota: {menornota[acessar]}')
    elif r == 3:
        print(f'media do ano: {mediaano[acessar]}')
    elif r == 4:
        print(f'todas as notas: {a[acessar]}')
    elif r == 5:
        print(f'resultado: {resultado[acessar]}')
    else:
        break
print('fim')
