risada = list(input())
i = 0
while i < len(risada):
    if risada[i] != "a" and risada[i] != "e" and risada[i] != "i" and risada[i] != "o" and risada[i] != "u":
        risada.remove(risada[i])
    else:
        i = i + 1
risada = "".join(risada)
if len(risada) % 2 == 0:
    meio = len(risada) // 2
    parte2 = list(risada[meio:])
else:
    meio = (len(risada) - 1) // 2
    parte2 = list(risada[meio + 1:])
parte1 = list(risada[0:meio])
parte2.reverse()
if parte1 == parte2:
    print("S")
else:
    print("N")
