n = int(input())
emails = []
verifica = []
for i in range(n):
    endereco, provider = input().split("@")
    endereco = endereco.split("+")[0]
    endereco = endereco.split(".")
    endereco = "".join(endereco)
    emails.append([endereco, provider])
for j in range(len(emails)):
    if emails[j] not in verifica:
        verifica.append(emails[j])
print(len(verifica))
