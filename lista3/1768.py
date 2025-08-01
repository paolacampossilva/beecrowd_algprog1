while True:
    try:
        n = int(input())
        asteriscos = 1
        espacos = int((n - 1) / 2)
        while asteriscos <= n:
            print((espacos * " ") + (asteriscos * "*"))
            asteriscos = asteriscos + 2
            espacos = espacos - 1
        print(int((n - 1) / 2) * " " + "*")
        print(int(((n - 1) / 2) - 1) * " " + "***")
        print()
    except EOFError:
        break
