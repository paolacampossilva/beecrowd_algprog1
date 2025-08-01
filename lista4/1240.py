n = int(input())
for i in range(n):
    a, b = input().split()
    encaixa = False
    if int(b) > int(a):
        encaixa = False
    elif a == b:
        encaixa = True
    elif a[len(a) - len(b):] == b:
        encaixa = True
    else:
        encaixa = False
    if encaixa:
        print("encaixa")
    else:
        print("nao encaixa")
