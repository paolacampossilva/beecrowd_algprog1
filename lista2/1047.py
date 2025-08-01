hora_inicial, minuto_inicial, hora_final, minuto_final = list(map(int, input().split()))
tempo_inicial = (hora_inicial * 60) + minuto_inicial
tempo_final = (hora_final * 60) + minuto_final
tempo = tempo_final - tempo_inicial
if tempo <= 0:
    tempo += 24 * 60
hora = tempo // 60
minuto = tempo % 60
print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")
