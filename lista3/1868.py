while True:
    try:
        n = int(input())
        if n == 0:
            break
        matriz = []
        for i in range(n):
            matriz.append(["O"] * n)
        y = n // 2
        x = y
        matriz[x][y] = "X"
        for linhas in matriz:
            print("".join(linhas))
        print("@")
        direcoes = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        incremeto = 1
        movimentos = 1
        indice_direcoes = 0
        while movimentos < n ** 2:
            for j in range(2):
                coordenada_x, coordenada_y = direcoes[indice_direcoes % 4]
                for k in range(incremeto):
                    if movimentos >= n ** 2:
                        break
                    matriz[x][y] = "O"
                    x = x + coordenada_x
                    y = y + coordenada_y
                    matriz[x][y] = "X"
                    for linhas in matriz:
                        print("".join(linhas))
                    print("@")
                    movimentos = movimentos + 1
                indice_direcoes = indice_direcoes + 1
            incremeto = incremeto + 1
    except EOFError:
        break
