maior = menor = qtd = 0
for i in range(1,6):
    num = int(input("digite um num: "))
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(menor, maior)