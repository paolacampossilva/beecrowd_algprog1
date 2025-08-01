valor = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
valor = int(valor * 100 + 0.5)
print("NOTAS:")
for nota in notas:
    qtd = valor // (nota * 100)
    print(f"{qtd} nota(s) de R$ {nota:.2f}")
    valor = valor - (qtd * (nota * 100))
print("MOEDAS:")
for moeda in moedas:
    qtd = valor // (moeda * 100)
    print(f"{round(qtd)} moeda(s) de R$ {moeda:.2f}")
    valor = valor - (qtd * (moeda * 100))
