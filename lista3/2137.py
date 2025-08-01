while True:
    try:
        n = int(input())
        lista = []
        for i in range(n):
            codigo = int(input())
            lista.append(codigo)
            lista.sort()
        for valor in lista:
            valor = str(valor)
            print(("0" * (4 - len(str(valor)))) + str(valor))
    except EOFError:
        break
