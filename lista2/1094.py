n = int(input())
ratos = 0
sapos = 0
coelhos = 0
for i in range(n):
    quantidade, categoria = input().split()
    quantidade = int(quantidade)
    if categoria == "R":
        ratos = ratos + quantidade
    elif categoria == "S":
        sapos = sapos + quantidade
    elif categoria == "C":
        coelhos = coelhos + quantidade
total = ratos + sapos + coelhos
percentual_ratos = (ratos * 100) / total
percentual_sapos = (sapos * 100) / total
percentual_coelhos = (coelhos * 100) / total
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
