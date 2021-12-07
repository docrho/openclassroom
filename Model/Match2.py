from Model.Player import Player

class Match:

    def __init__(self, joueur1: Player, joueur2: Player,
                 score1: str, score2: str):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score_joueur1 = score1
        self.score_joueur2 = score2

    def match(self):
        matches = ([self.joueur1, self.score_joueur1],
                   [self.joueur2, self.score_joueur2])
        return matches


