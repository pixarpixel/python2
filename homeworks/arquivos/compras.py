compras = [
'Batata',
'Chocolate',
'Pao',
'Requeijao',
'Frios',
'Ovo']

with open('listadecompras.txt', 'w+') as arquivo:
    arquivo.write('''=================================
          Lista do Diego
  Criada em: 30 de Setembro de 2022
=================================\n''')
    for item in compras:
        arquivo.write(f'{item}\n')
