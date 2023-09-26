language = ['Python', 'Javascript', 'Java', 'PHP', 'C++', 'Cobol']

#initialison de la variable index à 0 pour l'ordre d'affichage
index = 0
# tant que index est plus petit que la longueur du tableau (len) alors la boucle continue jusque la fin
# index  est incrémenté de 1 à chaque passage de la boucle et indique la position à lire
while index < len(language):
    print(language[index])
    # += est équivalent index + 1 et = permet de mettre la valeur de la variable index à jour
    index += 1
