n = int(input())
velocidade = list(map(int, input().split()))
indice = 0
for i in range(len(velocidade) - 1):
    if velocidade[i] > velocidade[i + 1]:
        indice = i + 2
        break
print(indice)
