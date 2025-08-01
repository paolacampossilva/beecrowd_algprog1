while True:
    try:
        resultado = 0
        m, n = map(int, input().split())
        lista = []
        lista.append(list(str(m)))
        lista.append(list(str(n)))
        if m != 0 and n != 0:
            for i in range(len(lista)):
                j = 0
                while j < len(lista[i]):
                    for digito in lista[i][j]:
                        if digito == "0":
                            lista[i].remove(lista[i][j])   
                        else:
                            j = j + 1 
                resultado = resultado + int("".join(lista[i]))
            resultado = list(str(resultado))
            k = 0
            while k < len(resultado):  
                    if resultado[k] == "0":
                        resultado.remove(resultado[k])   
                    else:
                        k = k + 1 
            print("".join(resultado))
    except EOFError:
        break
