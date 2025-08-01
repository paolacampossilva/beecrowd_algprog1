def primo(x):
    inicio = 2
    while inicio <= int(x ** 0.5):
        if x % inicio < 1:
            return False
        inicio = inicio + 1
    return True
n = int(input())
identificadores = list(map(int,input().split()))
primos = []
for i in range(len(identificadores)):
    if primo(identificadores[i]):
        if identificadores[i] > 1:
            primos.append(identificadores[i])
codigo = max(identificadores) + 1
while True:
    contador = 0
    for i in range(len(primos)):
        if codigo % primos[i] == 0:
            contador = contador + 1
    if contador == 0:
        break
    codigo = codigo + 1
print(codigo)
