dia_inicial = int((input().split())[1])
hora_inicial, minuto_inicial, segundo_inicial = map(int, input().split(":"))
dia_final = int((input().split())[1])
hora_final, minuto_final, segundo_final = map(int, input().split(":"))
tempo_inicial = (dia_inicial * 24 * 3600) + (hora_inicial * 3600) + (minuto_inicial * 60) + segundo_inicial
tempo_final = (dia_final * 24 * 3600) + (hora_final * 3600) + (minuto_final * 60) + segundo_final
tempo = tempo_final - tempo_inicial
dia = tempo // (24 * 3600)
hora = (tempo % (24 * 3600)) // 3600
minuto = ((tempo % (24 * 3600)) % 3600) // 60
segundo = ((tempo % (24 * 3600)) % 3600) % 60
print(f"{dia} dia(s)")
print(f"{hora} hora(s)")
print(f"{minuto} minuto(s)")
print(f"{segundo} segundo(s)")
