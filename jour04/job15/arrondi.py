liste = [22.4, 4.0, 16.22, 9.10, 11.00,12.22, 14.20, 5.20, 17.50]

def arrondi(liste):
    nliste = [] 
    for i in liste:
        i_chaine = str(i)
        indexpoint = i_chaine.index('.')
        i_arrondi = int(i_chaine[:indexpoint])
        nliste.append(i_arrondi)

    n = 0 
    for _ in nliste:
        n += 1 
    for i in range(1, n): 
        element = nliste[i]
        j = i-1 
        while j >= 0 and nliste[j] > element: 
            nliste[j+1] = nliste[j] 
            j -= 1
        nliste[j+1] = element
    print(nliste)

arrondi(liste)

