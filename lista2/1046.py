inicial, final = list(map(int, input().split()))
horas = 0
if inicial > final:
    for i in range(inicial, 24):
        horas += 1
    for i in range(0, final) :
        horas += 1
elif final > inicial:
    for i in range(inicial, final):
        horas += 1
elif inicial == final:
    horas = 24
print(f"O JOGO DUROU {horas} HORA(S)")
