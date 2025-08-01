n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print(f"Media: {media:.1f}")
if media < 5:
    print("Aluno reprovado.")
elif 5 <= media < 7:
    print("Aluno em exame.")
    ne = float(input())
    print(f"Nota do exame: {ne:.1f}")
    media_final = (media + ne) / 2
    if media_final >= 5:
        print("Aluno aprovado.")
    elif media_final < 5:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")
elif 7 <= media:
    print("Aluno aprovado.")
