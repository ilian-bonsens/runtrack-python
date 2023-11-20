saisie = int(input("Entrez l'investissement de départ : "))

montant = saisie
TRA = 1.03

print (f"""Investissement : {montant}
Taux rendement annuel : {(TRA-1)*100}%
Gain annuel : {(montant*TRA)-montant}""")

print ("Augmentation du capital de 5000, donc augmentation du taux de 2%.")

montant2 = montant+30+5000
TRA2 = TRA+0.02

print (f"""Investissement : {montant2}
Taux rendement annuel : {(TRA2-1)*100}%
Gain annuel : {(montant2*TRA2)-montant2}""")

print ("L'investisseur retire '10%' du capital total, le taux baisse de 1%.")

montant3 = ((montant2+300)*0.9)
TRA3 = TRA2-0.01

print (f"""Investissement : {montant3}
Taux rendement annuel : {(TRA3-1)*100}%
Gain annuel : {(montant3*TRA3)-montant3}""")