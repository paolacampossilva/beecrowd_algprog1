c = int(input())
for i in range(c):
    sequencia = ""
    a, b = map(int, input().split())
    for n in range(a, b + 1):
        sequencia = sequencia + str(n)
    invertido = list(sequencia)
    invertido.reverse()
    invertido = "".join(invertido)
    espelho = sequencia + invertido
    print(int(espelho))
