n = int(input())
contador = ""
for i in range(n):
    sobrenome = input()
    nome = list(sobrenome.lower())
    for letra in nome:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            contador = contador + "v"
        else:
            contador = contador + "c"
    if "ccc" in contador:
        print(f"{sobrenome} nao eh facil")
    else:
        print(f"{sobrenome} eh facil")
    contador = ""
