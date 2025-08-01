t = int(input())
for i in range(t):
    possibilidades = 1
    senha = input()
    senha = senha.lower()
    for char in senha:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "s":
            j = 1
        else:
            j = 0
        possibilidades = possibilidades * (2 + j)
    print(possibilidades)
