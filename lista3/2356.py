while True:
    try:
        dna = input()
        resistencia = input()
        if resistencia in dna:
            print("Resistente")
        else:
            print("Nao resistente")
    except EOFError:
        break
