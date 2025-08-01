casos = int(input())
for i in range(casos):
    linhas = int(input())
    soma = 0
    for e in range(linhas):
        string = input()
        for p in range(len(string)):
            a = ord(string[p]) - ord('A')
            soma = soma + a + e + p
    print(soma)
