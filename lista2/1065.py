valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
valor4 = int(input())
valor5 = int(input())
numeros = [valor1, valor2, valor3, valor4, valor5]
i = 0
for numero in numeros:
    if numero % 2 == 0:
        i = i + 1

print(f"{i} valores pares")
