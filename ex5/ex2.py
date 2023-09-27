#variable prénom
firstname = input("Quel est ton prénom?")
#fonction
def helloYou(firstname):
    my_name = firstname
    return f"Bonjour {my_name}."
#afficher
print(helloYou(firstname))
