genoma = input().strip()
virus = input().strip()
i = 0
while i < len(genoma) and i < len(virus) and genoma[i] == virus[i]:
    i = i + 1
indice_genoma = len(genoma) - 1
indice_virus = len(virus) - 1
while indice_genoma >= i and indice_virus >= i and genoma[indice_genoma] == virus[indice_virus]:
    indice_genoma = indice_genoma - 1
    indice_virus = indice_virus - 1
comprimento_minimo = (indice_virus - i + 1)
print(comprimento_minimo)
