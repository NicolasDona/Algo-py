# Variable attendu
array_note = ['8', '6']

# Fonction
def average(array_note):
    #Variable qui stocke la somme des notes
    avg = 0
    #Variable qui parcours l'index
    count = 0
    #boucle jusqu'à la fin de l'index
    while count < len(array_note):
        # Ajout de la note (convertie en entier) à la variable avg
        avg += int(array_note[count])
        # +1 sur la variable count pour passer à l'élément suivant de la liste
        count += 1
    return avg / len(array_note)

# affichage
print(average(array_note))
