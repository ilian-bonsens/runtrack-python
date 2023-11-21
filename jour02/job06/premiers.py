for N in range(2, 1001):
    for i in range(2, N): 
        if (N % i) == 0:
            break
    else:
        print(N)

#nombre premier n'est devisible que par lui même et par 1, avec for i in range(2, N): if (N % i) == 0 break#
#on cherche les nombres divisibles par autre que 1 et eux mêmes, et on ne print que le reste qui renvoie#
#aux nombres premiers#