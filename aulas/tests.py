def prepararAcai(ing1: str, ing2: str, ing3: str):
    itens = list()
    itens.append(ing1)
    itens.append(ing2)
    itens.append(ing3)
    return itens 

ingredientes = list()
for i in range(3):
    ingredientes.append(str(input('Digite um ingrediente: ')))
print(prepararAcai(ingredientes[0], ingredientes[1], ingredientes[2]))
