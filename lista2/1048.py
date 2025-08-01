salario = float(input())
if 0 <= salario <= 400.00:
    percentual = 15
elif 400.01 <= salario <= 800.00:
    percentual = 12
elif 800.01 <= salario <= 1200.00:
    percentual = 10
elif 1200.01 <= salario <= 2000.00:
    percentual = 7
elif salario > 2000.00:
    percentual = 4
reajuste = (percentual / 100) * salario
novo_salario = salario + reajuste
print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
