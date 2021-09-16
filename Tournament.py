import Player


class Tournament:
    def __init__(self, name: str, place: str, date: str, nb_turn: int,
                 players: list[Player], time: str, description: str,
                 doc_id : int = ""
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

    def __str__(self):
        return f"{self.name} {self.date}"

    def status(self):
        return
