valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())
valor5 = float(input())
valor6 = float(input())
numeros = [valor1, valor2, valor3, valor4, valor5, valor6]
i = 0
for numero in numeros:
    if numero > 0:
        i = i + 1
print(f"{i} valores positivos")
