while True:
    n = int(input())
    if n == 0:
        break
    soma = 0
    if n % 2 != 0:
        n = n + 1
    for i in range(n, n + 10, 2):
        soma = soma + i
    print(soma)
