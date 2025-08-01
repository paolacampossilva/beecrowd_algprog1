j = 2
for i in range(1, 10):
    if i % 2 != 0:
        j = j + 5
        for n in range(0, 3):
            print(f"I={i} J={j}")
            j = j - 1
