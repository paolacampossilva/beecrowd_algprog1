while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        num = input()
        cadeia = ""
        qte_zero = 0
        qte_um = 0
        zero = True
        for j in range(len(num)):
            if zero:
                qte_zero = qte_zero + int(num[j])
                zero = False
            else:
                qte_um = qte_um + int(num[j])
                zero = True
        qte_zero = list(str(qte_zero))
        qte_um = list(str(qte_um))
        p = 0
        while len(qte_zero) > 1:
            qte_zero[p] = int(qte_zero[p]) + int(qte_zero[p + 1])
            qte_zero.remove(qte_zero[p + 1])
        while len(qte_um) > 1:
            qte_um[p] = int(qte_um[p]) + int(qte_um[p + 1])
            qte_um.remove(qte_um[p + 1])
        qte = int(qte_zero[0]) + int(qte_um[0])
        print(qte)
