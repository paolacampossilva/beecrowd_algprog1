valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
valor4 = int(input())
valor5 = int(input())
numeros = [valor1, valor2, valor3, valor4, valor5]
par = 0
impar = 0
negativo = 0
positivo = 0
for numero in numeros:
    if numero % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    
    if numero > 0:
        positivo = positivo + 1
    elif numero < 0:
        negativo = negativo + 1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")
