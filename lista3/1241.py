n = int(input())
encaixa = False
for i in range(n):
    x = []
    a, b = input().split()
    a = list(a)
    b = list(b)
    if len(b) > len(a):
        encaixa = False
    else:
        for j in range(len(b), 0, -1):
            x.append(a[len(a) - j])
        if x == b:
            encaixa = True
        else:
            encaixa = False
    if encaixa:
        print("encaixa")
    else:
        print("nao encaixa")
