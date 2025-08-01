num1, num2, num3 = map(int, input().split())
maior_1_2 = (num1 + num2 + abs(num1 - num2)) / 2
if maior_1_2 == num1:
    maior = (num1 + num3 + abs(num1 - num3)) / 2
else:
    maior = (num2 + num3 + abs(num2 - num3)) / 2
print(f"{int(maior)} eh o maior")
