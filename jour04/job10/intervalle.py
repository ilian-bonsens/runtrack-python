L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

def inter():
    result = 1 #on créé une variable de valeur 1#
    for num in L:
        if 24 < num < 91:
            result = num * result 
#la boucle va répéter cette opération pour chaque num compris dans cette intervalle et incrémenter le result#

    return result

print(inter())