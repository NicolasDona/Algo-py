
age = int(input("Entrez votre âge : "))

if 8 <= age <= 9:
    cat = "Microbe"
elif 1 <= age <= 7:
    cat = "Trop petit"
elif 10 <= age <= 11:
    cat = "Poussin"
elif 12 <= age <= 13:
    cat = "Benjamin"
elif 14 <= age <= 15:
    cat = "Minime"
elif 16 <= age <= 17:
    cat = "Cadette/Cadet"
elif 18 <= age <= 19:
    cat = "Junior"
elif 20 <= age <= 39:
    cat = "Sénior"
else:
    cat = "Vétérane/Vétéran"
    
    # if(age >= 8 and age <=9)
    # category = "Microbe" 


print(f"Votre catégorie est : {cat}")