direcoes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
linhas, colunas = map(int, input().split())
matriz = []
achei = False
for m in range(linhas):
    linha = list(map(int, input().split()))
    matriz.append(linha)
for i in range(linhas):
    for j in range(colunas):      
        if matriz[i][j] == 42:
            cont = 0
            for k in range(len(direcoes)):
                dx = i
                dy = j
                dx = dx + direcoes[k][0]
                dy = dy + direcoes[k][1]
                if 0 <= dx < linhas and 0 <= dy < colunas:
                    if matriz[dx][dy] == 7:
                        cont = cont + 1
                    else:
                        break
            if cont == 8:
                achei = True
                break
    if achei:
        break
if achei:
    print(i + 1, j + 1)
else:
    print(0, 0)
