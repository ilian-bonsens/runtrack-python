cote1 = int(input("Entrez une longueur pour le triangle :"))
cote2 = int(input("Entrez une largeur pour le triangle :"))
cote3 = int(input("Entrez une hauteur pour le triangle :"))

if cote1 == cote2 == cote3:
    print("Ceci est un triangle équilatéral.")
elif cote1 ** 2 == (cote2 ** 2 + cote3 ** 2) or cote2 ** 2 == (cote1 ** 2 + cote3 ** 2) or cote3 ** 2 == (cote1 ** 2 + cote2 ** 2):
    if cote1 == cote2 or cote1 == cote3 or cote2 == cote3: #si vérifie les 2 conditions alors rectangle isocèle#
        print("Ceci est un triangle rectangle isocèle.")
    else: #si ne vérifie que la première condition du elif alors seulement rectangle#
        print("Ceci est un triangle rectangle.")
elif cote1 == cote2 or cote1 == cote3 or cote2 == cote3:
    print("Ceci est un triangle isocèle.")

