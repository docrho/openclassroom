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

    def tour1(self, tournament_players: Player()):
        self.name = 'Round1'
        sorted_players_list_by_rank = sorted(tournament_players,
                                             key=itemgetter("ranking"))
        for seq in range(4):

            self.match_list.append((
                Player(
                    sorted_players_list_by_rank[seq]['lastname'],
                    sorted_players_list_by_rank[seq]['first_name'],
                    sorted_players_list_by_rank[seq]['birth_date'],
                    sorted_players_list_by_rank[seq]['gender'],
                    sorted_players_list_by_rank[seq]['ranking'],
                    sorted_players_list_by_rank[seq]['points'],
                ),
                sorted_players_list_by_rank[seq]['points'],
                Player(
                    sorted_players_list_by_rank[seq+4]['lastname'],
                    sorted_players_list_by_rank[seq+4]['first_name'],
                    sorted_players_list_by_rank[seq+4]['birth_date'],
                    sorted_players_list_by_rank[seq+4]['gender'],
                    sorted_players_list_by_rank[seq+4]['ranking'],
                    sorted_players_list_by_rank[seq+4]['points'],
                ),
                sorted_players_list_by_rank[seq+4]['points'],
            ))
        return self.match_list

    def tour2(self, tournament_players):
        self.name = 'Round'
        sorted_players_list_by_point = sorted(tournament_players,
                                              key=itemgetter("points"))
        self.match_list = []
        for seq in range(4):

            self.match_list.append((
                Player(
                    sorted_players_list_by_point[seq]['lastname'],
                    sorted_players_list_by_point[seq]['first_name'],
                    sorted_players_list_by_point[seq]['birth_date'],
                    sorted_players_list_by_point[seq]['gender'],
                    sorted_players_list_by_point[seq]['ranking'],
                    sorted_players_list_by_point[seq]['points'],
                ),
                sorted_players_list_by_point[seq]['points'],
                Player(
                    sorted_players_list_by_point[seq+4]['lastname'],
                    sorted_players_list_by_point[seq+4]['first_name'],
                    sorted_players_list_by_point[seq+4]['birth_date'],
                    sorted_players_list_by_point[seq+4]['gender'],
                    sorted_players_list_by_point[seq+4]['ranking'],
                    sorted_players_list_by_point[seq+4]['points'],
                ),
                sorted_players_list_by_point[seq+4]['points'],
            ))
        return self.match_list
        # ajouter condition if point sont egal alors par rank

    # adding result prompt from view to all match from match list

    def add_score_to_match(self, score_from_view: list):
        match_list_update = []
        x = 0
        for match in self.match_list:
            current_match_list = list(match)
            current_match_list[1] = current_match_list[1] + score_from_view[x]
            current_match_list[3] = current_match_list[3]+ score_from_view[x+1]
            current_match_list = tuple(current_match_list)
            match_list_update.append(current_match_list)
            x += 2
        self.match_list = match_list_update
        return self.match_list
