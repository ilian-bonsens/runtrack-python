def doublons():
    liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    nliste = []
    for i in liste:
        if i not in nliste:
            nliste.append(i)
    return nliste
#compare les deux listes, si i n'est pas deja dans nliste, on l'y met ; s'il n'y est pas on passe au reste#


print(doublons())
