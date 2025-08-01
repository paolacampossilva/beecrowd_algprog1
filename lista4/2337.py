import math
fibonacci = [0] * 43
fibonacci[1] = 1
fibonacci[2] = 1
for i in range(3, 43):
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2] 
while True:
        try:
            n = int(input())
            numerador = fibonacci[n + 2] 
            denominador = 2 ** n
            maximo_divisor_comum = math.gcd(numerador, denominador)
            numerador_simplificado = numerador // maximo_divisor_comum
            denominador_simplificado = denominador // maximo_divisor_comum
            print(f"{numerador_simplificado}/{denominador_simplificado}")
        except EOFError:
             break
