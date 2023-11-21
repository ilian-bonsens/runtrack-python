s = "abcdefghijklmnopqrstuvwxyz" * 10
i = 1
while len(s) > 0:
    line = s[:2*i-1] 
#le premier nb correspond au départ du découpage, si on ne met rien il commence au début#
#le dernier donne nb de caractère de la ligne, ici 2*i-1 = 1 si i = 1 puis 3 si i = 2 et ainsi de suite#
#cela nous permet de rajouter 2 par deux#
    print(line)
    s = s[2*i-1:]
#on enlève de la chaine de caractère le nb de caractère utilisé dans la ligne précédente#
    i = i + 1


