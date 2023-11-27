liste = [64, 74, 25, 50, 22, 11, 99]

def tri(liste):
    n = 0 # compte elemnts dans la liste
    for _ in liste:
        n += 1 
    for i in range(1, n): #commence au 2e élément
        element = liste[i] #on met l'élément à trier dans une var
        j = i-1 #on met l'index de l'élément précédent dans une autre var
        while j >= 0 and liste[j] > element: #tant que l'élément précédent est positif et > à l'élément actuel
            liste[j+1] = liste[j] #on déplace l'élément précédent vers la droite dans l'index
            j -= 1 #on décrémente j pour repasser à l'élément précédent
        liste[j+1] = element #on place l'élément que nous avions pris au départ dans l'espace vide créé par le mouvement vers la droite
    return liste


print(tri(liste))