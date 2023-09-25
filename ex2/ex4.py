# exercice : Un magasin de reprographie facture 0,10 € l'unité les dix premières photocopies, 0,09 € les vingt suivantes et 0,08 € au-delà.


cop_numb = int(input("Entrez le nombre de photocopies à effectuer : "))

# Initialiser le coût total à 0
cout_total = 0.0

# boucle pour les 10 premières photocopies
if cop_numb <= 10:
    cout_total = cop_numb * 0.10
else:
    cout_total = 10 * 0.10  # Coût des 10 à 0.10 € chacune

    # boucle pour les 20 photocopies suivantes
    if cop_numb <= 30:
        cout_total += (cop_numb - 10) * 0.09
    else:
        cout_total += 20 * 0.09 

        # +30
        cout_total += (cop_numb - 30) * 0.08

# Afficher la facture correspondante
print(f"Le coût total pour {cop_numb} photocopies est de {cout_total:.2f} €.")
