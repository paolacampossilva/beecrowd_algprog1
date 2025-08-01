n = int(input())
for n in range(0, n):
    x = int(input())
    if x % 2 == 0 and x != 0:
        par_impar = "EVEN"
    elif x % 2 != 0 and x != 0:
        par_impar = "ODD"
    else:
        par_impar = ""
    if x > 0:
        positivo_negativo = "POSITIVE"
    elif x < 0:
        positivo_negativo = "NEGATIVE"
    else: 
        positivo_negativo = "NULL"
    if par_impar:
        print(f"{par_impar} {positivo_negativo}")
    else:
        print(f"{positivo_negativo}")
