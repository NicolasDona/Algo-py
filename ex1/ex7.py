
ht = 120
number = 10
tva = 20

# Conversion en float (pour permettre des calculs décimaux)
ht = float(ht)
number = int(number)
tva = int(tva)

# Calcul du total HT
total_ht = ht * number

# Calcul du montant de la TVA
montant_tva = (total_ht * tva) / 100

# Calcul du montant total TTC (avec TVA)
total_ttc = total_ht + montant_tva

print(f"Le total HT est de {total_ht} euros.")
print(f"Le montant de la TVA est de {montant_tva} euros.")
print(f"Le total TTC (avec TVA) est de {total_ttc} euros.")


# ht = 120
# number = 10
# tva = 20
# ht = int(ht)
# number = int(number)
# tva = int(tva)
# total =  ht * number
# print (f"notre total est {total + tva}")
