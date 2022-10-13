a = dict()
al = soma = menor = maior = 0
no = []

al = input('Aluno(a): ')
a.update({al: []})
for i in range (1, 5):
    n = int(input(f'Nota {i}°: '))
    no.append(n) if n <= 10 else print('nota inválida.')
    a[al].append(n) #notas todas dict
    #decidir maior e menor num
    no.sort()
    maior = no[-1]
    menor = no[0]
    media = sum(no)/len(no)

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
        print(f'maior nota: {maior}') 
    elif r == 2:
        print(f'menor nota: {menor}')
    elif r == 3:
        print(f'media do ano: {media}')
    elif r == 5:
        if media > 6:
            print('Aprovado!')
        elif media == 6:
            print('Recuperação!')
        else:
            print('Reprovado!')
    elif r == 4:
        print(f'todas as notas: {a}')
    elif r == 6: 
        break
print('fim')


'''
a = {
    'camila' : [1, 2, 3, 4]
    'julia': [0, 5, 4, 4]
}
maior = {
    'camila': [4]
    'julia': [4]
}
menor = {
    'camila': [0]
    'julia': [1]
}
'''