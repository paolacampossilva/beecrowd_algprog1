while True:
    try:
        pessoas, qte_datas = map(int, input().split())
        datas = []
        resposta = "Pizza antes de FdI"
        achei = False
        for i in range(qte_datas):
            data, sep, presenca = input().partition(" ")
            datas.append(data)
            presenca = presenca.split()
            contador = 0
            for j in range(pessoas):
                if presenca[j] == "1":
                    contador = contador + 1
            if (contador == pessoas) and (not achei):
                resposta = datas[i]
                achei = True
        print(resposta)
    except EOFError:
        break
