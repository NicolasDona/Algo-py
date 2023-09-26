# Variable attendu
#variable number en "entier"
number = int(input("1-Addition ou 2-Soustraction (1 ou 2)"))

#boucle tant que un chiffre correct n'est pas donné - variable plus grande que 2 ou plus petite que 1
while number > 2 or number < 1:
    #si mauvais afficher le msg et reposer la question
    print("Le chiffre que vous avez donné n'est pas 1 ou 2.")
    number = int(input("Donne-moi un chiffre entre 1 et 2 : "))
