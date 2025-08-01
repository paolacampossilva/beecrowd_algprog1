lista1 = input().split()
lista2 = input().split()
chave = input()
if chave == "nao":
    lista = lista1 + lista2
else:
    segundo = False
    lista_s = []
    lista_p = []
    for i in range(len(lista1)):
        if lista1[i] == chave:
            lista_s.append(lista1[i])
            segundo = True
        elif segundo:
            lista_s.append(lista1[i])
        else:
            lista_p.append(lista1[i])
    lista = lista_p + lista2 + lista_s
for j in range(len(lista)):
    if j == len(lista) - 1:
        print(lista[j])
    else:
        print(lista[j], end=" ")
