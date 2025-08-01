while True:
    try:
        string = input()
        frase = ""
        maiuscula = False
        for i in range(0, len(string)):
            if string[i] == " ":
                frase = frase + " "
            elif maiuscula:
                frase = frase + (string[i].lower())
                maiuscula = False
            elif not maiuscula:
                frase = frase + (string[i].upper())
                maiuscula = True
        print(frase)
    except EOFError:
        break
