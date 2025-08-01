while True:
    try:
        string = input()
        if string == "" or string == (" " * len(string)):
            print()
        else:
            frase = []
            alfabeto = "abcdefghijklmnopqrstuvwxyz"
            for j in range(len(string)):
                if string[j] not in frase and string[j] != " ":
                    frase.append(string[j])
            frase.sort()
            frase = "".join(frase)
            intervalos = []
            intervalo = 0
            for inicio in range(len(frase)):
                fim = inicio + 1
                if intervalo == frase:
                    break
                while fim < len(frase) + 1:
                    if intervalo == frase:
                        break
                    if frase[inicio:fim] in alfabeto:
                        intervalo = frase[inicio:fim]
                        if len(intervalos) != 0 and intervalo in intervalos[len(intervalos) - 1]:
                            break
                        if len(intervalos) == 0:
                            intervalos.append(intervalo)
                        elif intervalo[0] == intervalos[len(intervalos) - 1][0]:
                            intervalos[len(intervalos) - 1] = intervalo
                        else:
                            intervalos.append(intervalo)
                        fim = fim + 1
                    else:
                        break
            for m in range(len(intervalos)):
                if m == len(intervalos) - 1:
                    print(f"{intervalos[m][0]}:{intervalos[m][len(intervalos[m]) - 1]}")
                else:
                    print(f"{intervalos[m][0]}:{intervalos[m][len(intervalos[m]) - 1]}", end=", ")
    except EOFError:
        break
