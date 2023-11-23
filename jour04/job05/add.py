def add():
    L = [3, 7, 76, 32, 9]
    print(L)
    print(L[1])
    L[3] = L[2] + L[4]
    print(L)
    return L[4]

print(add())