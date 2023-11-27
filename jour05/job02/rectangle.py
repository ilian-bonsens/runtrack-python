def dessiner_rectangle(width, height):
    print('|' + '-' * (width - 2) + '|')
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')
    print('|' + '-' * (width - 2) + '|')
#sans les ajustements avec les  - 2 car nos | pour les cotés rajoutent deux unités à la width
#les deux | des cotés se rajoutent à ceux de la height, on en retire 2 pour revenir à la height de base

dessiner_rectangle(7, 6)
