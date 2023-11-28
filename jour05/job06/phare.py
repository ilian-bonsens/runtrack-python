def phare(marches, hauteur):
    distance = ((hauteur * 2) * 5) * 7
    return f"Pour {marches} marches de {hauteur} centimètres, le gardien parcours {distance:.2f}m par semaine"

print(phare(19, 6.768))