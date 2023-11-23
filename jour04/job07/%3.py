def multiple():
    L = [8, 24, 48, 2, 16]
    return sum(1 for num in L if num % 3 == 0)
#pour chaque multiple de 3 trouvé dans L, il prend la valeur 1 et on en fait la somme à la fin ce qui les decompte#

print(multiple())