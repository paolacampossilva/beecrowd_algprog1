vogais = ["a", "e", "i", "o", "u"]
simbolos = ["@", "&", "!", "*", "#"]
while True:
    try:
        frase = list(input())
        for i in range(len(frase)):
            for j in range(len(simbolos)):
                if frase[i] == simbolos[j]:
                    frase[i] = vogais[j]
                    break
        print("".join(frase))    
    except EOFError:
        break
