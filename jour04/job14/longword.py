def my_long_word(n, chaine):
    mots_longs = []
    mot = ''
    longueur_mot = 0

    for caractere in chaine:
        if caractere == ' ': #induit que les espaces sont tjrs la fin d'un mot
            if longueur_mot > n:
            #si la longueur du mot courant est supérieure à n, ajouter le mot à la liste des mots longs
                mots_longs.append(mot)
            #remet à 0 pour recommencer pour tous les mots
            mot = ''
            longueur_mot = 0
        else:
        #si le caractère n'est pas un espace, ajouter le caractère au mot courant et incrémenter la longueur du mot courant
            mot += caractere
            longueur_mot += 1

    # Après avoir parcouru tous les caractères, vérifier une dernière fois si le dernier mot est long
    if longueur_mot > n:
        mots_longs.append(mot)

    return mots_longs

print(my_long_word(4, "Je possède une playstation 5 depuis plusieurs blablabla"))
