pedras, sapos = map(int, input().split())
rio = [0] * pedras
for i in range(sapos):
    posicao, pulo = map(int, input().split())
    posicao = posicao - 1
    for j in range(posicao, -1, -pulo):
        if rio[j] == 0:
            rio[j] = 1
    for j in range(posicao, pedras,pulo):
        if rio[j] == 0:
            rio[j] = 1
for k in range(len(rio)):
    print(rio[k])
