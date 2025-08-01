dicionario = {2 : "abc", 3 : "def", 4 : "ghi", 5 : "jkl", 6 : "mno", 7 : "pqrs", 8 : "tuv", 9 : "wxyz"}
n = int(input())
for i in range(n):
    palavra = input()
    sequencia = []
    for k in range(len(palavra)):
        j = 2
        letra = palavra[k]
        while j < 10:
            if letra.lower() in dicionario[j]:
                index = list(dicionario[j]).index(letra.lower())
                num = (index + 1) * str(j)
                if letra != letra.lower():
                    num = "#" + num
                sequencia.append(num)
                break
            elif letra == " ":
                    num = "0"
                    sequencia.append(num)
                    break
            else:
                j = j + 1
    for l in range(len(sequencia)):
        if l != len(sequencia) - 1:
            if sequencia[l + 1][0] != "#":
                if sequencia[l][0] == sequencia[l + 1][0]:
                    sequencia[l] = sequencia[l] + "*"
                elif sequencia[l][0] == "#" and sequencia[l][1] == sequencia[l + 1][0]:
                    sequencia[l] = sequencia[l] + "*"
    print("".join(sequencia))
