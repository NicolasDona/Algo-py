#variable number en "entier"
number = int(input("Donne-moi un chiffre entre 10 et 20 : "))
#limite le choix de réponse entre 10 et 20
while number < 10 or number > 20:
    #Si en dessous de 10
    if number < 10:
        print("Trop petit")
        number = int(input("Donne-moi un chiffre entre 10 et 20 : "))
    #sinon
    else:
        print("Trop grand")
    number = int(input("Donne-moi un chiffre entre 10 et 20 : "))
#number validation / Sortie de boucle
print("Merci, vous avez donné un chiffre valide :", number)
