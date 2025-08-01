l0 = list(input())
l1 = list(input())
l2 = list(input())
l3 = list(input())
l = [l0, l1, l2, l3]
c = []
j = 0
while j < len(l0):
    c0 = []
    for i in range(len(l)):
        c0.append(l[i][j]) 
    c.append(int("".join(c0)))
    j = j + 1
codigo = []
for k in range(1, len(c) - 1):
    char = (c[0] * c[k] + c[len(c) - 1]) % 257
    codigo.append(char)
for n in range(len(codigo)):
    codigo[n] = chr(codigo[n])
print("".join(codigo))
