c = int(input())
for i in range(c):
    resposta = input().split()
    if resposta[0] == resposta[1]:
        print("empate")
    elif "tesoura" in resposta and "papel" in resposta:
        if resposta[0] == "tesoura":
            print("rajesh")
        elif resposta[1] == "tesoura":
            print("sheldon")
    elif "papel" in resposta and "pedra" in resposta:
        if resposta[0] == "papel":
            print("rajesh")
        elif resposta[1] == "papel":
            print("sheldon")
    elif "pedra" in resposta and "lagarto" in resposta:
        if resposta[0] == "pedra":
            print("rajesh")
        elif resposta[1] == "pedra":
            print("sheldon")
    elif "lagarto" in resposta and "spock" in resposta:
        if resposta[0] == "lagarto":
            print("rajesh")
        elif resposta[1] == "lagarto":
            print("sheldon")
    elif "spock" in resposta and "tesoura" in resposta:
        if resposta[0] == "spock":
            print("rajesh")
        elif resposta[1] == "spock":
            print("sheldon")
    elif "tesoura" in resposta and "lagarto" in resposta:
        if resposta[0] == "tesoura":
            print("rajesh")
        elif resposta[1] == "tesoura":
            print("sheldon")
    elif "lagarto" in resposta and "papel" in resposta:
        if resposta[0] == "lagarto":
            print("rajesh")
        elif resposta[1] == "lagarto":
            print("sheldon")
    elif "papel" in resposta and "spock" in resposta:
        if resposta[0] == "papel":
            print("rajesh")
        elif resposta[1] == "papel":
            print("sheldon")
    elif "spock" in resposta and "pedra" in resposta:
        if resposta[0] == "spock":
            print("rajesh")
        elif resposta[1] == "spock":
            print("sheldon")
    elif "pedra" in resposta and "tesoura" in resposta:
        if resposta[0] == "pedra":
            print("rajesh")
        elif resposta[1] == "pedra":
            print("sheldon")
