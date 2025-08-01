dia_inicial = int(list(input().split())[1])
hora_inicial, minuto_inicial, segundo_inicial = list(map(int, input().split(":")))
dia_final = int(list(input().split())[1])
hora_final, minuto_final, segundo_final = list(map(int, input().split(":")))

tempo_inicial = (dia_inicial * 86400) + (hora_inicial * 3600) + (minuto_inicial * 60) + segundo_inicial
tempo_final = (dia_final * 86400) + (hora_final * 3600) + (minuto_final * 60) + segundo_final
tempo = abs(tempo_final - tempo_inicial)
dia = tempo // 86400
hora = (tempo % 86400) // 3600
minuto = ((tempo % 86400) % 3600) // 60
segundo = ((tempo % 86400) % 3600) % 60

print(f"{dia} dia(s)")
print(f"{hora} hora(s)")
print(f"{minuto} minuto(s)")
print(f"{segundo} segundo(s)")
