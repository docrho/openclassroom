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
        self.match_list = []
        for seq in range(4):

            self.match_list.append((
                Player(
                    tournament_players[seq].lastname,
                    tournament_players[seq].first_name,
                    tournament_players[seq].birth_date,
                    tournament_players[seq].gender,
                    tournament_players[seq].ranking,
                    tournament_players[seq].point,
                ),
                tournament_players[seq].point,
                Player(
                    tournament_players[seq+3].lastname,
                    tournament_players[seq+3].first_name,
                    tournament_players[seq+3].birth_date,
                    tournament_players[seq+3].gender,
                    tournament_players[seq+3].ranking,
                    tournament_players[seq+3].point,
                ),
                tournament_players[seq+3].point,
            ))
        return self.match_list

    def tour2(self, tournament_players):
        self.name = 'Round'
        self.match_list = []
        for seq in range(4):

            self.match_list.append((
                Player(
                    tournament_players[seq]['lastname'],
                    tournament_players[seq]['first_name'],
                    tournament_players[seq]['birth_date'],
                    tournament_players[seq]['gender'],
                    tournament_players[seq]['ranking'],
                    tournament_players[seq]['points'],
                ),
                tournament_players[seq]['points'],
                Player(
                    tournament_players[seq+3]['lastname'],
                    tournament_players[seq+3]['first_name'],
                    tournament_players[seq+3]['birth_date'],
                    tournament_players[seq+3]['gender'],
                    tournament_players[seq+3]['ranking'],
                    tournament_players[seq+3]['points'],
                ),
                tournament_players[seq+3]['points'],
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
