import Player
import json

class Tournament:
    def __init__(self, name: str = "", place: str = "",
                 date: str = "", nb_turn: int = "",
                 players: list[Player] = "", time: str = "",
                 description: str = "", doc_id: int = ""
                 ):
        self.name = name
        self.place = place
        self.date = date
        self.nb_turn = nb_turn
        self.players = players
        self.time = time
        self.description = description
        self.rounds_list = []
        self.tours_list = []
        self.doc_id = doc_id
        ####attribute from method
        self.tournament_list = []
        self.all_tournament_list = []
        self.players_in_tournament = []

    def __str__(self):
        return f"{self.name} {self.date}"

    def status(self):
        return
    def get_all_players_in_tournament(self,):
        return self.tournament_list

    def tournament_instance_list(self,all_tournament):
        self.tournament_list = []
        for tournament_data in all_tournament:
            self.tournament_list.append(
                Tournament(
                    tournament_data["name"],
                    tournament_data["place"],
                    tournament_data["date"],
                    tournament_data["nb_turn"],
                    tournament_data["players"],
                    tournament_data["time"],
                    tournament_data["description"],
                    tournament_data.doc_id,
                )

            )
        return self.tournament_list

    def tournament_instance(self, tournament):
        self.tournament_list = []
        self.tournament_list.append(
            Tournament(
                tournament["name"],
                tournament["place"],
                tournament["date"],
                tournament["nb_turn"],
                tournament["players"],
                tournament["time"],
                tournament["description"],
                tournament.doc_id,
            )

        )
        return self.tournament_list

