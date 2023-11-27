def diagonale(n):
    print('+' + '-' * (n + 2) + '+')
    print('|' + '#' * (n + 1) + ' |')
    for i in range(n + 1):
        print('|' + '#' * (n - i) + " " + '#' * (i + 1) + '|')
    print('+' + '-' * (n + 2) + '+')

diagonale(9)