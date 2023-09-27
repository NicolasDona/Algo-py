def my_calcul(operation, *numbers):
# variable qui stocke le résultat
    if operation == "addition":
        result = 0
        for number in numbers:
            result = result + number
        return result
    elif operation == "soustraction":
        substraction = numbers[0]
        for number in numbers[1:]:
            substraction = substraction-number
        return substraction
# Appelle la fonction my_calcul avec les arguments saisis
print(my_calcul("soustraction", 3, 2))