while True:
    try:
        string = input().lower().split()
        anterior = False
        contador = 0
        for i in range(len(string) - 1):
            if string[i][0] == string[i + 1][0] and not anterior:
                contador = contador + 1
                anterior = True
            elif string[i][0] != string[i + 1][0]:
                anterior = False
        print(contador)
    except EOFError:
        break
