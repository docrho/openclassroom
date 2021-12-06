from operator import itemgetter
from Model.Player import Player

class Match:

    def __init__(self, tournament_player: list):

        self.player1 = Player()
        self.player2 = Player()
        #########
        self.tournament_players = tournament_player

    def set_color(self):
        self.player1.color = "black"
        self.player2.color = "white"
        return True

    def first_match(self):
        sorted_list = sorted(self.tournament_players,
                             key=itemgetter("ranking"))
        players_match = {}
        match = []
        i = 0
        while i <= 3:
            players_match["players"] = [sorted_list[i], sorted_list[i+4]]
            players_match["score"] = ["0", "0"]
            match.append(players_match)
            i += 1
        return match

    def match_list_generator(self, match_list):

        return match_list

    def tour(self):
        print()
