def triangle():
    hauteur = int(input("Hauteur : "))
    for i in range(hauteur - 1): # - 1 pour que cela ne print pas la derniere ligne
        print(" " * (hauteur - i - 1) + "/" + " " * (2 * i) + "\\")
        #(hauteur - i - 1) calcule le nb d'espace en sachant que la premiere unite est à index 0
        #(2 * i) agrandi l'espace entre les /\ en fonction de l'index du premier /
    print("/" + "__" * (hauteur - 1) + "\\")#print la dernire ligne

triangle()



