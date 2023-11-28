def cesar(n, chaine):
    resultat = "" #nouvelle chaine dans laquelle on met les mots décalés
    for caractere in chaine: #remet les espaces à leur place
        if caractere == ' ':
            resultat += ' '
        else:
            decalage = ord(caractere) + n 
#ord transforme le caractere en son code en nombre, on touche à ce code en nombre pour changer le caractere
            if decalage < ord('a'):
                decalage += 26 
            #pour decaler en negatif apres a, on rajoute 26 ce qui fait bien revenir sur le z
            elif decalage > ord('z'):
                decalage -= 26 #et inversement
            resultat += chr(decalage) #chr reconverti les nombres en caracteres
    print(resultat)

cesar(-5, "Ceci est une phrase de test")

