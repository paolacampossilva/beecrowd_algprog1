c = int(input())
for i in range(c):
    string = input()
    a, b = string.split("mek")
    qte = (len(list(a.split("h")[1]))) * len(list(b.split("me")[0]))
    resposta = "k" + ("a" * qte)
    print(resposta)
