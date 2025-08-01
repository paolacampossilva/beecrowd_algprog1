i = 0
x = 0
for n in range(0, 100):
    valor = int(input())
    if valor > i:
        i = valor
        x = n + 1
print(i)
print(x)
