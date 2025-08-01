n = int(input())
teto = list(map(int, input().split()))
chao = list(map(int, input().split()))
t = -1
c = -1
for i in range(n):
    if (teto[i] == 0) or (i + 1 != n and teto[i] == 1 and teto[i + 1] == 2):
        t = i
        break
    if (chao[i] == 0) or (i + 1 != n and chao[i] == 1 and chao[i + 1] == 2):
        c = i 
        break
if t < c:
    status = "teto"
else:
    status = "chao"
mudancas = 0
j = 0
while j < n:
    if status == "teto":
        if (j + 1 != n and teto[j] != 0 and teto[j + 1] == 0) or (j + 1 != n and teto[j] == 1 and teto[j + 1] == 2):
            status = "chao"
            mudancas = mudancas + 1
        else:
            j = j + 1
    elif status == "chao":
        if (j + 1 != n and chao[j] != 0 and chao[j + 1] == 0) or (j + 1 != n and chao[j] == 1 and chao[j + 1] == 2):
            status = "teto"
            mudancas = mudancas + 1
        else:
            j = j + 1
print(mudancas)
