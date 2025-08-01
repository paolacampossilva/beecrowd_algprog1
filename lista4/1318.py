while True:
    originais, presentes = map(int, input().split())
    if originais == 0 and presentes == 0:
        break
    copias = 0
    bilhetes = list(map(int, input().split()))
    ori = []
    cop = []
    for i in range(len(bilhetes)):
        if bilhetes[i] not in ori:
            ori.append(bilhetes[i])
        elif bilhetes[i] not in cop:
            cop.append(bilhetes[i])
            copias = copias + 1
    print(copias)
