codigo, quantidade = input().split(" ")
codigo = int(codigo)
quantidade = int(quantidade)
if codigo == 1:
    valor_unitario = 4
elif codigo == 2:
    valor_unitario = 4.5
elif codigo == 3:
    valor_unitario = 5
elif codigo == 4:
    valor_unitario = 2
elif codigo == 5:
    valor_unitario = 1.5
valor_total = valor_unitario * quantidade
print(f"Total: R$ {valor_total:.2f}")
