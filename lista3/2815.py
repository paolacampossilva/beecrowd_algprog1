string = input().split()
for i in range(len(string)):
    if string[i][0:2] == string[i][2:4]:
        string[i] = string[i][2:]
print(" ".join(string))
