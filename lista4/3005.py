testes = int(input())
for t in range(testes):
    a1,a2,a3,b1,b2,b3 = map(int,input().split())
    dimensoes_a = sorted([a1,a2,a3])
    dimensoes_b = sorted([b1,b2,b3])
    dimensoes_a.reverse()
    dimensoes_b.reverse()
    copia_a = dimensoes_a.copy()
    copia_b = dimensoes_b.copy()
    contador_a = 0 
    contador_b = 0
    for i in range(3):
        for j  in range(3):
            if dimensoes_a[i] > copia_b[j] and copia_b[j] > 0:
                contador_a += 1
                copia_b[j] = -1
                dimensoes_a[i] = -1
            if dimensoes_b[i] > copia_a[j] and copia_a[j] > 0:
                contador_b += 1
                copia_a[j] = -1
                dimensoes_b[i] = -1
    contador_a = contador_a // 2
    contador_b = contador_b // 2
    status = 0
    if contador_a > 0:
        status = 2 
    if contador_b > 0:
        status = 1
    if contador_a > 0 and contador_b > 0:
        status = 3
    print(status)
