chave = "LRUD"
while True:
    linhas, colunas, ins = map(int, input().split())
    if linhas == 0 and colunas == 0 and ins == 0:
        break
    matriz = []
    achei = False
    for i in range(linhas):
        matriz.append(list(input()))
        if (not achei) and (i != 0) and (i != linhas - 1):
            for j in range(1, colunas - 1):
                if matriz[i][j] == "<":
                    l = i
                    c = j
                    achei = True
                    break
    instrucoes = list(input())
    pastilhas = 0
    game = [False, True, False, False]
    for k in range(ins):
        if instrucoes[k] != "W":
            game = [False, False, False, False]
            game[chave.index(instrucoes[k])] = True
        else:
            if game[0]:
                if matriz[l][c - 1] == "*":
                    pastilhas = pastilhas + 1
                    matriz[l][c - 1] = " "
                if matriz[l][c - 1] != "#":
                    c = c - 1
            elif game[1]:
                if matriz[l][c + 1] == "*":
                    pastilhas = pastilhas + 1
                    matriz[l][c + 1] = " "
                if matriz[l][c + 1] != "#":
                    c = c + 1
            elif game[2]:
                if matriz[l - 1][c] == "*":
                    pastilhas = pastilhas + 1
                    matriz[l - 1][c] = " "
                if matriz[l - 1][c] != "#":
                    l = l - 1
            elif game[3]:
                if matriz[l + 1][c] == "*":
                    pastilhas = pastilhas + 1
                    matriz[l + 1][c] = " "
                if matriz[l + 1][c] != "#":
                    l = l + 1
    print(pastilhas)
