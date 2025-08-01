a, b, c = list(map(float, input().split()))
for i in range(3):
    if b > a:
        b, a = a, b
    if c > b:
        b, c = c, b
    if c > a:
        c, a = a, c
if a >= (b + c):
    print("NAO FORMA TRIANGULO")
elif (a ** 2) == (b ** 2) + (c ** 2):
    print("TRIANGULO RETANGULO")
elif (a ** 2) > (b ** 2) + (c ** 2):
    print("TRIANGULO OBTUSANGULO")
elif (a ** 2) < (b ** 2) + (c ** 2):
    print("TRIANGULO ACUTANGULO")
if a == b and b == c and c == a:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c:
    print("TRIANGULO ISOSCELES")
