valor = int(input())
hora = valor / 3600
min = "0." + (str(hora)).split(".")[1]
minuto = float(min) * 60
seg = "0." + (str(minuto)).split(".")[1]
segundo = float(seg) * 60
print(f"{int(hora)}:{int(minuto)}:{segundo:.0f}")
