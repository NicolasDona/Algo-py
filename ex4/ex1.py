#variable number en "entier"
number = int(input("Donne-moi un chiffre entre 1 et 3 : "))

#boucle tant que un chiffre correct n'est pas donné - variable plus grande que 3 ou plus petite que 1
while number > 3 or number < 1:
    #si mauvais afficher le msg et reposer la question
    print("Le chiffre que vous avez donné n'est pas entre 1 et 3.")
    number = int(input("Donne-moi un chiffre entre 1 et 3 : "))
#number validation / Sortie de boucle
print("Merci, vous avez donné un chiffre valide :", number)