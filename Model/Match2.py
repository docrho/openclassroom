from Model.Player import Player

class Match:

    def __init__(self, joueur1: Player, joueur2: Player):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score_joueur1 = joueur1.point
        self.score_joueur2 = joueur2.point

    def match(self):
        matche = ([self.joueur1, self.score_joueur1],
                   [self.joueur2, self.score_joueur2])
        return matche


