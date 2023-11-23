def inter():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    return sum(num for num in L if num > 24 and num < 91)

print(inter())