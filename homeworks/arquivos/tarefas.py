
with open('tarefas.txt', 'w+') as arquivo:
    arquivo.write(f'''{'='*30}
      Lista de tarefas
{'='*30}\n''')
    print('escreva suas tarefas (enter/0 para finalizar): ')
    while True:
        tarefa = input('')
        if tarefa == '' or tarefa == '0':
            break
        arquivo.write(f'{tarefa}\n')
