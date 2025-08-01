nome_vendedor = input("")
salario_fixo = float(input(""))
valor_total_vendas = float(input(""))
comissao = (15/100) * valor_total_vendas
salario = salario_fixo + comissao
print(f"TOTAL = R$ {salario:.2f}")
