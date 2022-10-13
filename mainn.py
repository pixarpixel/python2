import gerenciar_txt
import os 
import time

print('Para começar, crie um arquivo.')
nome = input('nome da lista: ')
criador = input('seu nome (nome do criador): ')
gerenciar_txt.criar(nome, criador)
print('arquivo criado!')
os.system('cls')

while True:
    print("""[1] - Criar novo arquivo 
[2] - Ler arquivo 
[3] - Escrever no arquivo   
[4] - Limpar o arquivo todo 
[5] - Remover item        
[6] - Ordenar alfabéticamente (a-z)
[7] - Deletar o arquivo
[8] - Finalizar o arquivo""")
    r = int(input(''))
    if r == 1:
        nome = input('nome da lista: ')
        criador = input('seu nome (nome do criador): ')
        gerenciar_txt.criar(nome, criador)
        print('arquivo criado!')
    elif r == 2: 
        gerenciar_txt.ler(nome)        
        input('\npressione enter para continuar')
    elif r == 3: 
        gerenciar_txt.escrever(nome)
        print('itens adicionados!')
    elif r == 4:
        gerenciar_txt.limpar(nome)
        print('arquivo limpo!')
    elif r == 5: 
        item = input('item que deseja remover: ')
        gerenciar_txt.limparitem(nome, item)
    elif r == 6:
        gerenciar_txt.ordem_alfabetica(nome)
        print('ordenado de a-z!')
    elif r == 7:
        gerenciar_txt.deletar(nome)
        print('arquivo deletado!')
    elif r == 8: 
        gerenciar_txt.finalizar(nome)
        print('finalizado.')
        break
    time.sleep(0.5)
    os.system('cls')

