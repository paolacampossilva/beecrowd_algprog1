valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())
valor5 = float(input())
valor6 = float(input())
valores = [valor1, valor2, valor3, valor4, valor5, valor6]
media = (valor1 + valor2 + valor3 + valor4 + valor5 + valor6) / 6
positivo = 0
soma = 0
for valor in valores:
    if valor > 0:
        positivo = positivo + 1
        soma = soma + valor
media = soma / positivo
print(f"{positivo} valores positivos")
print(f"{media:.1f}")
