while True:
    try:
        linhas, colunas = map(int, input().split())
        soma = 0
        for i in range(linhas):
            linha = list(map(int, input().split()))
            for j in range(colunas):
                soma = soma + linha[j]
        sacas = soma // 60
        litros = soma % 60
        print(f"{sacas} saca(s) e {litros} litro(s)")
    except EOFError:
        break
