#le while true execute la boucle tant qu'une erreur est détectée#
while True:
    try:
        num1 = int(input("Entrez un nombre de minutes :"))
        break #vient casser la boucle quand il n'y a pas d'erreur dans l'input#
    except ValueError:
        print("Entrez un nombre entier.") #message d'erreur#

def time_to_text(num1):
    heures = num1 // 60
    minutes_restantes = num1 % 60
    return f"{heures} heures et {minutes_restantes} minutes"
#creation de la fonction et affichage du resultat de celle ci#

print(time_to_text(num1))


