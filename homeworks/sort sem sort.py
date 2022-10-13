l = []
for i in range(5):
    num = int(input("digite um número: "))
    # pos = posicao/cada for  x = ultimo num
    for pos, x in enumerate(l):
        if num < x:
            l.insert(pos, num)
            print(f'o número foi adicionado na posição {pos}')
            break
    else:
        l.append(num)
        print('foi adicionado no fim da lista')
print("lista", l)