nom = "montre"
prix = 100
stock = 10

print (f"""Article : {nom}
Prix : {prix}
Stock : {stock}""")

saisie = int(input("Entrez la quantité que vous souhaitez acheter : "))

print (f"""Article : {nom}
Prix : {prix*1.1}
Stock : {stock-saisie}""")