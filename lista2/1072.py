n = int(input())
dentro = 0
fora = 0
for n in range(0, n):
    x = int(input())
    if 10 <= x <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1
print(f"{dentro} in")
print(f"{fora} out")
