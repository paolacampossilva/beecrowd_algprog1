while True:
    try:
        equacao = input().split("+")
        equacao.extend(equacao[1].split("="))
        equacao.remove(equacao[1])
        if equacao[2] == "J":
            print(int(equacao[0]) + int(equacao[1]))
        elif equacao[1] == "L":
            print(int(equacao[2]) - int(equacao[0]))
        elif equacao[0] == "R":
            print(int(equacao[2]) - int(equacao[1]))
    except EOFError:
        break
