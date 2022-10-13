import os
from datetime import date

def criar(nome, criador):
    arquivo = open(f'{nome}.txt','w')
    arquivo.write(f'''{'='*30}
    Criada por {criador} 
    em {date.today()}
{'='*30}\n''')

def ler(arquivo: str):
    with open(f'{arquivo}.txt', 'r') as arquivo:
        arquivo.seek(0)
        print(arquivo.read())

def escrever(arquivo: str):
    with open(f'{arquivo}.txt', 'a') as arquivo:
        print('escreva suas compras (enter/0 para finalizar): ')
        while True:
            texto = input('')
            if texto == '' or texto == '0':
                break
            arquivo.write(texto + '\n')

def limpar(arquivo: str): 
    open(f'{arquivo}.txt', 'w').close()

def limparitem(file: str, _item: str):
    item = f'{_item}\n'
    try:
        with open(f'{file}.txt', 'r+') as arquivo:
            titulo = []        
            for i in range(1, 5):
                titulo.append(arquivo.readline())
            itens = arquivo.readlines() 
            itens.remove(item)
            open(f'{file}.txt', 'w').close()
            arquivo.seek(0)
            arquivo.writelines(titulo)
            arquivo.writelines(itens)
            print('item removido!')
    except ValueError:
        a = input('este valor nao existe.\ndeseja ler o arquivo? s/n\n')
        if a == 's':
            ler(file)

def ordem_alfabetica(arquivo: str):
    with open(f'{arquivo}.txt', 'r+') as file:
        titulo = []        
        for i in range(1, 5):
            titulo.append(file.readline())
        linhas = file.readlines()
        linhas.sort()
        file.seek(0)
        file.writelines(titulo)
        file.writelines(linhas)

def deletar(arquivo: str): 
    os.remove(f'{arquivo}.txt')

def finalizar(arquivo):
    file = open(f'{arquivo}.txt', 'r')
    file.close()
