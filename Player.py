class Player:

    def __init__(self, last_name="", first_name="", birth_date="", gender="",
                 ranking="", point=0, doc_id=""):
        self.lastname = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.point = point
        self.doc_id = doc_id

    def __str__(self):
        return self.lastname

    def __repr__(self):
        return self.lastname

    def player_id_checking(self, ids: list, all_players):
        all_id = self.get_all_players_id(all_players)
        for id in ids:
            if str(id) not in str(all_id):
                return False
        return True

    def list_all_players(self, all_player_data):
        player_list = []
        for player_data in all_player_data:
            player_list.append(Player(
                player_data["lastname"],
                player_data["first_name"],
                player_data["birth_date"],
                player_data["gender"],
                player_data["ranking"],
                player_data["points"],
                player_data.doc_id
                                      )
                               )
        return player_list

    def get_all_players_in_tournament(self, tournament_id: int):

        tournament = self.tournament.get(doc_id=tournament_id)
        players_deserialized = json.loads(tournament["players"])
        return players_deserialized

    def get_all_players_id(self, all_players):
        all_id = []
        for player in all_players:  # taking all id
            all_id.append(player.doc_id)
        return all_id