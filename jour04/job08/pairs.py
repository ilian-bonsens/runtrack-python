def somme():
    L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    return sum(num for num in L if num % 2 == 0)
#si les nombres dans L sont des multiples de 2, fait la somme des nombres#

print(somme())