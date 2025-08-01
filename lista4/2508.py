tabela = ["AJS", "BKT", "CLU", "DMV", "ENW", "FOX", "GPY", "HQZ", "IR"]
while True:
    try:
        nome = list(input().upper())
        soma = 0
        for n in range(len(nome)):
            if nome[n] == " ":
                continue
            achei = False
            for t in range(len(tabela)):
                for i in range(len(tabela[t])):
                    if nome[n] == tabela[t][i]:
                        soma = soma + t + 1
                        achei = True
                        break
                if achei:
                    break
        soma = str(soma)
        while len(soma) > 1:
            s = 0
            for i in range(len(soma)):
                s = s + int(soma[i])
            soma = str(s)
        print(soma)
    except EOFError:
        break
