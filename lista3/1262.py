while True:
    try:
        string = input()
        qte = int(input())
        contador = 0
        processos = 0
        i = 0
        while i < (len(string)):
            if string[i] == "W":
                contador = contador + 1
            else:
                for j in range(i, len(string)):
                    if string[j] == "R":
                        processos = processos + 1
                    else:
                        contador = contador + 1
                        processos = 0
                        break
                    if processos > qte:
                        contador = contador + 1
                        processos = processos - qte
                    i = j
            i = i + 1
        if processos != 0:
            contador = contador + 1
        print(contador)
    except EOFError:
        break
