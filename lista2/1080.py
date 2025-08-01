valores = []
for n in range(0, 100):
    valor = int(input())
    valores.append(valor)
maior = max(valores)
posicao = valores.index(maior) + 1
print(maior)
print(posicao)
