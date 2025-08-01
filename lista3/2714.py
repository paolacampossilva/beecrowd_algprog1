n = int(input())
for i in range(n):
    registro = input()
    if registro[0:2] != "RA" or len(registro) != 20:
        print("INVALID DATA")
    else:
        for j in range(2, len(registro)):
            if registro[j] != "0":
                posicao = j
                break
        print(registro[j:])
