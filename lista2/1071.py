x = int(input())
y = int(input())
soma = 0
if x > y:
    passo = -1
else:
    passo = 1
for num in range(x + passo, y, passo):
    if num % 2 != 0:
        soma = soma + num
print(soma)
