#le try dit quelle commande on veut executer, si elle se s'execute pas bien, cela affiche notre message#
try:
    num1 = int(input("Entrez une heure :"))
except ValueError:
    print("Entrez un nombre entier positif.")
try:
    num2 = int(input("Entrez des minutes :"))
except ValueError:
    print("Entrez un nombre entier positif.")

def time_to_text(num1, num2):
    if num1 > 23 :
        return "Veuillez entrer un nombre inférieur à 24."
    if num2 > 59 :
        return "Veuillez entrer un nombre inférieur à 60."
    else:
        return f"{num1} heures et {num2} minutes."

time_to_text(num1, num2)

print(time_to_text(num1, num2))

