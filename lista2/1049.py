a = input()
b = input()
c = input()
if a == "vertebrado" and b == "ave" and c == "carnivoro":
    animal = "aguia"
elif a == "vertebrado" and b == "ave" and c == "onivoro":
    animal = "pomba"
elif a == "vertebrado" and b == "mamifero" and c == "onivoro":
    animal = "homem"
elif a == "vertebrado" and b == "mamifero" and c == "herbivoro":
    animal = "vaca"
elif a == "invertebrado" and b == "inseto" and c == "hematofago":
    animal = "pulga"
elif a == "invertebrado" and b == "inseto" and c == "herbivoro":
    animal = "lagarta"
elif a == "invertebrado" and b == "anelideo" and c == "hematofago":
    animal = "sanguessuga"
elif a == "invertebrado" and b == "anelideo" and c == "onivoro":
    animal = "minhoca"
print(animal)
