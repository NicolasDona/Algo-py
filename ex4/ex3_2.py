# variable de départ
nb_start = int(input("Entrez un nombre de départ : "))
# Compteur
count = 1
#Tant que la variable est inférieur ou égale à 10 la boucle recommence
while count <= 10:
    #Affiche le résultat
    print(nb_start + count)
    # += est équivalent index + 1 et = permet de mettre la valeur de la variable index à jour
    count += 1