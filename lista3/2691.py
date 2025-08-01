n = int(input())
for i in range(n):
    entrada = input().split("x")
    for k in range(len(entrada)):
        if entrada[k] != "x":
            entrada[k] = int(entrada[k])
    if entrada[0] == entrada[1]:
        for j in range(5, 11):
            print(f"{entrada[0]} x {j} = {entrada[0] * j}")
    else:
        for j in range(5, 11):
            print(f"{entrada[0]} x {j} = {entrada[0] * j} && {entrada[1]} x {j} = {entrada[1] * j}")
