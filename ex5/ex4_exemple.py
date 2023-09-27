# Définition de la fonction my_calcul
def my_calcul(operation, *numbers):
    # Si l'opération est une addition ou le symbole '+'
    if operation == "addition" or operation == "+":
        # Retourne la somme des chiffres
        return sum(numbers)
    # Si l'opération est une soustraction ou le symbole '-'
    elif operation == "soustraction" or operation == "-":
        # Initialise le résultat avec le premier chiffre
        result = numbers[0]
        # Boucle sur les chiffres suivants
        for num in numbers[1:]:
            # Soustrait chaque chiffre du résultat
            result -= num
        # Retourne le résultat final
        return result
    # Si l'opération n'est reconnue ni comme addition ni comme soustraction
    # else:
    #     # Lève une exception indiquant une opération invalide
    #     raise ValueError("L'opération doit être 'addition' ou 'soustraction' ou '+' ou '-'")

# Demande à l'utilisateur de saisir le type d'opération
# L'utilisateur peut entrer soit les mots "addition" ou "soustraction", soit les symboles '+' ou '-'
operation = input("Veuillez entrer le type d'opération (addition/soustraction/+/-): ")

# Demande à l'utilisateur de saisir les chiffres
# L'utilisateur doit entrer les chiffres séparés par des espaces
chiffres = input("Veuillez entrer les chiffres séparés par des espaces: ")

# Convertit la chaîne de chiffres en une liste d'entiers
# La méthode split() divise la chaîne en une liste de sous-chaînes (basé sur les espaces)
# https://www.w3schools.com/python/ref_string_split.asp
# La fonction map() applique la fonction int() à chaque sous-chaîne pour la convertir en entier
# numbers = list(map(int, chiffres.split()))
print(result)

# Appelle la fonction my_calcul avec les arguments saisis
# Le préfixe * décompresse la liste numbers en arguments individuels pour la fonction
# print(my_calcul(operation, *numbers))