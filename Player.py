import json

class Player:

    def __init__(self, last_name="", first_name="", birth_date="", gender="",
                 ranking="", point = 0, doc_id=""):
        self.lastname = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.point = point
        self.doc_id = doc_id
        #attribute report from method
        self.all_players = []
        self.all_players_id = []
        # serialized list of player from database
        self.serialized_players_list = []
        self.players_list = []
    def __str__(self):
        return self.lastname

    def __repr__(self):
        return self.lastname

    def append_player_from_id(self, player_from_database):
        self.players_list.append(
            player_from_database
        )
        return self.players_list

    def serialize_player(self,):
        self.serialized_players_list = json.dumps(self.players_list)
        return self.serialized_players_list

    def player_id_checking(self, ids: list): # checking if id exist
        all_id = self.get_all_players_id(self.all_players)
        for id in ids:
            if str(id) not in str(all_id):
                return False
        return True

    def list_all_players(self, all_player_data):
        self.all_players = []
        for player_data in all_player_data:
            self.all_players.append(Player(
                player_data["lastname"],
                player_data["first_name"],
                player_data["birth_date"],
                player_data["gender"],
                player_data["ranking"],
                player_data["points"],
                player_data.doc_id
                                      )
                               )
        return self.all_players

    def get_all_players_id(self, all_players):

        for player in all_players:  # taking all id
            self.all_players_id.append(player.doc_id)
        return self.all_players_id
    