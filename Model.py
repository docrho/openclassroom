import json

from tinydb import TinyDB, Query
from tinydb.operations import set
from tinydb import where
import Player
import Round
import Tournament


class DbManager(TinyDB):

    def __init__(self):
        self.db = TinyDB("db.json")
        self.players = self.db.table("players")
        self.tournament = self.db.table('tournament')

    def get_all_players(self):
        all_players = self.players.all()
        return all_players

    def get_all_players_in_tournament(self, tournament_id: int):

        tournament = self.tournament.get(doc_id=tournament_id)
        players_deserialized = json.loads(tournament["players"])
        return players_deserialized

    def get_all_players_id(self):
        all_players = self.players.all()
        all_id = []
        for player in all_players:  # taking all id
            all_id.append(player.doc_id)
        return all_id

    def player_id_checking(self, ids: list):
        all_id = self.get_all_players_id()
        for id in ids:
            if str(id) not in str(all_id):
                return False
        return True
#        if for not broken return true

    def _store_player(self, player):
        self.players.insert({
            "type": "player", "lastname": player.lastname, "first_name": player.first_name,
            "birth_date": player.birth_date, "gender": player.gender, "ranking": player.ranking, "points": player.point,
        })

    def add_player(self, players_data, player):
        for player_data in players_data:

            if player_data['lastname'] == player.lastname and player_data['first_name'] == player.first_name and \
                    player_data['birth_date'] == player.birth_date:
                return False
        self._store_player(player)
        return True

    def store_tournament(self, tournament):
        self.tournament.insert({
            "name": tournament.name, "place": tournament.place,
            "date": tournament.date, "nb_turn": tournament.nb_turn, "players": tournament.players,
            "time": tournament.time, "description": tournament.description,"rounds_list": tournament.rounds_list,
            "tours_list":tournament.tours_list
        })

    def remove_players(self, lastname, birth_date):
        if self.players.remove(where('lastname') == str(lastname) and where('birth_date') == str(birth_date)):
            return True
        else:
            return False

    def remove_tournament(self, id):
        if self.tournament_id_check(int(id)): # check if the tournament id exist
            self.tournament.remove(doc_ids=[int(id), ])#remove the tournament if exist
            return True
        else:
            return False # otherwise return false

    def list_all_players(self):
        return self.players.all()

    def tournament_id_check(self, id):
        list_id = []
        all_tournaments = self.tournament.all()
        for tournament in all_tournaments:
            list_id.append(tournament.doc_id)
        if id in list_id:
            return True
        else:
            return False

    def update_tournament(self, key, id, update):
        self.tournament.update(set(key, update), doc_ids=[int(id)])
