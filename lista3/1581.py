n = int(input())
for i in range(n):
    linguas = []
    pessoas = int(input())
    for j in range(pessoas):
        idioma = input()
        linguas.append(idioma)
    for k in range(1, len(linguas)):
        if linguas[0] != linguas[k]:
            lingua = "ingles"
            break
        else:
            lingua = linguas[0]
    print(lingua)
