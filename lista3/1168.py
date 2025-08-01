n = int(input())
lista = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for i in range(n):
    leds = 0
    num = list(input())
    for j in range(len(num)):
        leds = leds + lista[int(num[j])]
    print(f"{leds} leds")
