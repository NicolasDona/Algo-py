nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))


# nombre > 0 vérifie si le deuxième nombre est strictement positif.
# nombre < 0 vérifie si le deuxième nombre est strictement négatif.
# bien faire la différence pour les deux cas entre les 2 ()
if (nombre1 > 0 and nombre2 > 0) or (nombre1 < 0 and nombre2 < 0):
    resultat = "positif"
else:
    resultat = "négatif"

print(f"Le produit de {nombre1} et {nombre2} est {resultat}.")