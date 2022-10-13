from xmlrpc.client import MultiCallIterator


a = dict()
media = dict()
menornota = dict()
maiornota = dict()
al = soma = menor = maior = qtd = 0
no = []
while True:
    al = input('Aluno(a): ')
    a.update({al: []})
    if al != 'fim': 
        # notas
        for i in range(1, 5):
            n = int(input(f'Nota {i}°: '))
            no.append(n) if n <= 10 else print('nota inválida.')
            a[al].append(n) #notas todas dict
            #decidir maior e menor num
            no.sort()
            maior = no[-1]
            menor = no[0]
            mediaano = sum(no)/len(a)
            #menor nota dict
            no.clear()

    if al == 'fim':
        a.pop('fim')
        break

# fim do while - menu do aluno
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
        print(f'media do ano: {media[acessar]}')
    elif r == 5:
        if media[acessar] > 6:
            print('Aprovado!')
        elif media[acessar] == 6:
            print('Recuperação!')
        else:
            print('Reprovado!')
    elif r == 4:
        print(f'todas as notas: {a[acessar]}')
    else: 
        break
print(a, menornota, maiornota, no)
