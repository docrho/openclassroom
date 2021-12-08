from Model.Match2 import Match
from operator import itemgetter
from Model.Player import Player

class Tour:

    def __init__(self):
        self.match_list = []
        self.name = ""
        self.start_time = ""
        self.start_Date = ""
        self.end_time = ""
        self.end_Date = ""

    def tour1(self, tournament_players):
        self.name = 'Round1'
        sorted_players_list_by_rank = sorted(tournament_players,
                             key = itemgetter("ranking"))
        i = 0
        while i<=3:

            self.match_list.append(Match(
                Player(
                    sorted_players_list_by_rank[i]['lastname'],
                    sorted_players_list_by_rank[i]['first_name'],
                    sorted_players_list_by_rank[i]['birth_date'],
                    sorted_players_list_by_rank[i]['gender'],
                    sorted_players_list_by_rank[i]['ranking'],
                    sorted_players_list_by_rank[i]['points'],
                ),
                Player(
                    sorted_players_list_by_rank[i+4]['lastname'],
                    sorted_players_list_by_rank[i+4]['first_name'],
                    sorted_players_list_by_rank[i+4]['birth_date'],
                    sorted_players_list_by_rank[i+4]['gender'],
                    sorted_players_list_by_rank[i+4]['ranking'],
                    sorted_players_list_by_rank[i+4]['points'],
                ),
            ))
            i+=1
        return self.match_list


    def tour2(self,tournament_players):
        self.name = 'Round2'
        sorted_players_list_by_point = sorted(tournament_players,
                                             key = itemgetter("points"))
        i = 0
        while i <= 3:
            self.match_list.append(Match(
                Player(
                    sorted_players_list_by_point[i]['lastname'],
                    sorted_players_list_by_point[i]['first_name'],
                    sorted_players_list_by_point[i]['birth_date'],
                    sorted_players_list_by_point[i]['gender'],
                    sorted_players_list_by_point[i]['ranking'],
                    sorted_players_list_by_point[i]['points'],
                ),
                Player(
                    sorted_players_list_by_point[i]['lastname'],
                    sorted_players_list_by_point[i]['first_name'],
                    sorted_players_list_by_point[i]['birth_date'],
                    sorted_players_list_by_point[i]['gender'],
                    sorted_players_list_by_point[i]['ranking'],
                    sorted_players_list_by_point[i]['points'],
                ),
            ))
            i += 1
            #ajouter condition if point sont egal alors par rank
        return

    def tour3(self):
        self.name = 'Round3'
        return

    def tour4(self):
        self.name = 'Round4'
        return

    #adding result prompt from view to all match from match list
    def add_score_to_match(self, score_from_view: list):
        for match in self.match_list:
            match.score_joueur1 = score_from_view[0]
            match.score_joueur2 = score_from_view[1]
        return self.match_list
