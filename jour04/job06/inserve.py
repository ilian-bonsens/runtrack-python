L = [1, 2, 3, 4, 5]

def inverse():
    print(L)
    L[0], L[-1] = L[-1], L[0]
    return L

print(inverse())