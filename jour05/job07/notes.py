import math

liste =[83, 51, 38, 79, 48]

def notes(liste):
    nliste = []
    for i in liste:
        if i > 40 and (math.ceil(i / 5.0) * 5 - i) < 3:
            i = math.ceil(i / 5.0) * 5
        nliste.append(i)
    print(nliste)

notes(liste)

