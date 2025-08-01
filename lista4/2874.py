while True:
    try:
        n = int(input())
        frase = []
        for i in range(n):
            binario = list(input().strip())
            decimal = 0
            for j in range(len(binario)):
                if binario[j] != "0" and binario[j] != "1":
                    continue
                decimal = decimal + (int(binario[j]) * (2 ** (len(binario) - 1 - j)))
            frase.append(chr(decimal))
        print("".join(frase))
    except EOFError:
        break
