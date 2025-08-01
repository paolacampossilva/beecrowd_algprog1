n = int(input())
pomekons = []
for k in range(n):
    pomekon = input()
    if pomekon not in pomekons:
        pomekons.append(pomekon)
print(f"Falta(m) {151 - len(pomekons)} pomekon(s).")
