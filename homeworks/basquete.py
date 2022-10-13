""""
Crie um programa que gerencie partidas de basquete, seu programa deve pedir o nome do jogador, 
quantas partidas ele jogou. Após passar o número de partidas, perguntar quantos pontos ele fez em cada partida.
Ao fim mostre em um dicionário dessa forma:
{
  'Jogador': 'LeBron',
  'Pontos': '[35, 29, 28, 15, 40]'
  'Total': 147
}
Nesse exemplo, eu reponderia 5 partidas.
"""
soma = 0
basquete = { 'Jogador': '',
'Pontos': [],
'Total': []}
nome = input('nome do jogador: ')
basquete.update({'Jogador': nome})
qtd = int(input('quantidade de partidas: ')) 
for i in range(1, qtd+1):
    pontos = int(input(f'quantos pontos na {i} partida?: '))
    basquete['Pontos'].append(pontos)
    soma += pontos
basquete.update({'Total': soma})
print(basquete)

