def moyenne(note1, note2, note3):
    return ((note1+note2+note3)/3)

moyenne_etudiant = moyenne(11,12,20)

if moyenne_etudiant > 14:
    print("Très bon élève.")
elif moyenne_etudiant > 10:
    print("Bon élève.")
elif moyenne_etudiant > 7:
    print("Élève moyen.")
else : 
    print("Élève qui doit faire des efforts.")