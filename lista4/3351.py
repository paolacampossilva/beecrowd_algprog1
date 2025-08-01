pessoas, alvo = map(int, input().split())
momento = []
incremento = []
for i in range(pessoas):
    a, b = map(int, input().split())
    momento.append(a)
    incremento.append(b)
contador = 0
while contador < alvo:
    i = momento.index(min(momento))
    j = momento[i]
    momento[i] = momento[i] + incremento[i]
    contador = contador + 1
print(j)
