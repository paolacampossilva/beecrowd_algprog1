n, m = map(int, input().split())
lista1 = []
lista2 = []
for i in range(n):
    l1, l2 = input().split()
    lista1.append(l1)
    lista2.append(l2)
for j in range(m):
    frase = list(input())
    for f in range(len(frase)):
        for l in range(len(lista1)):
            if frase[f] == lista1[l]:
                frase[f] = lista2[l]
            elif frase[f] == lista2[l]:
                frase[f] = lista1[l]
    print("".join(frase))
