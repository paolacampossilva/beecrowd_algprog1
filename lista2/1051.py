salario = float(input())
if 0 <= salario <= 2000:
    print("Isento")
else: 
    if 2000 < salario <= 3000:
        imposto = (salario - 2000) * (8 / 100)
    elif 3000 < salario <= 4500:
        imposto = (1000 * (8 / 100)) + ((salario - 3000) * (18 / 100))
    elif salario > 4500:
        imposto = (1000 * (8 / 100)) + (1500 * (18 / 100)) + ((salario - 4500) * (28 / 100))
    print(f"R$ {imposto:.2f}")
