n = int(input())
for i in range(n):
    num = int(input())
    soma = 0
    for j in range(1, num):
        if num % j == 0:
            soma = soma + j
    if num == soma:
        print(f"{num} eh perfeito")
    else:
        print(f"{num} nao eh perfeito")
