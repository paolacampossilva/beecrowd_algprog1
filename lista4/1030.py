casos = int(input())
for j in range(casos):
    num, incremento = map(int, input().split())
    seguro = 0
    for i in range(2, num + 1):
        seguro = (seguro + incremento) % i
    print(f"Case {j + 1}: {seguro + 1}")
