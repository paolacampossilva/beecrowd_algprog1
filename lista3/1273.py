pular = False
while True:
    try:
        lista = []
        n = int(input())
        if n == 0:
            break
        if pular:
            print()
        for i in range(n):
            linha = input()
            linha = linha.strip()
            linha = linha.split()
            lista.append(" ".join(linha))
            maior = 0
        for j in range(len(lista)):
            if len(lista[j]) > maior:
                maior = len(lista[j])
        for k in range(n):
            print((maior - len(lista[k])) * " " + lista[k])
        pular = True
    except EOFError:
        break
