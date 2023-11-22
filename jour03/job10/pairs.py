def pair(num):
    if not isinstance(num,int) or num == 0:
        print("Entrez un nombre entier non nul.")
    elif num % 2 == 0:
        print("Nombre pair.")
    else:
        print("Nombre impair.")
    
pair(17)