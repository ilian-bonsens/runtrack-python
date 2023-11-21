cote1 = int(input("Entrez une longueur pour le triangle :"))
cote2 = int(input("Entrez une largeur pour le triangle :"))
cote3 = int(input("Entrez une hauteur pour le triangle :"))

if cote1 == cote2 or cote1 == cote3 or cote3 == cote2:
    print("Ceci est un triangle isocèle")
