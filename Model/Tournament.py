from Model.Player import Player
from Model.Tour import Tour
import json
from Model.Db import DbManager
from operator import itemgetter



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
        self.players = []
        self.time = time
        self.description = description
        #round already played
        self.rounds_list = []
        self.current_tour = Tour()
        self.tours_list = []
        self.doc_id = doc_id
        ####attribute from method
        self.tournament_list = []
        self.all_tournament_list = []
        self.players_in_tournament = []
        self.tournament_info = []
        self.db = DbManager()

    def __str__(self):
        return f"{self.name} {self.date}"
    def add_tournament_info(self,tournament_info, serialized_players_list):
        self.name = tournament_info['name']
        self.place = tournament_info['place']
        self.date = tournament_info['date']
        self.time = tournament_info['time']
        self.description = tournament_info['description']
        self.place = tournament_info['place']
        self.players = serialized_players_list

    def _all_tournament_instance(self, all_tournament):
        for tournament_data in all_tournament:
            self.all_tournament_list.append(
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
        return self.all_tournament_list

    def tournament_instance(self, tournament):
        self.name = tournament["name"]
        self.place = tournament["place"]
        self.date = tournament["date"]
        self.nb_turn = tournament["nb_turn"]
        #deserialising player from databse
        players_deserialised = json.loads(tournament["players"])
        #instancing player
        for player in players_deserialised:
            self.players.append(Player(
                player["lastname"],
                player["first_name"],
                player["birth_date"],
                player["gender"],
                player["ranking"],
                player["points"],
            ))
        self.time = tournament["time"]
        self.description = tournament["description"]
        self.doc_id = tournament.doc_id
        return True

    def remove_tournament(self, id: int()):
        self.db.remove_tournament(id)

    def list_all_tournament(self):
        return self._all_tournament_instance(self.db.tournament.all())

    def tournament_id_checking(self, id):
        return self.db.tournament_id_check(id)

    def get_tournament_by_id(self, id):
        return self.db.tournament.get(doc_id= id)

    def store_tour_already_played(self):
        self.rounds_list = self.current_tour.match_list
        return self.rounds_list

#a terminer car quand les players sont trié differement le resultat ne sera pa le meme
    def store_player_data_from_match(self,):
        player_dict ={
            "lastname":[],
            "first_name":[],
            "birth_date":[],
            "gender":[],
            "ranking":[],
            "points":[],
        }
        for player in self.players:
            player_dict["lastname"].append(player.lastname)
            player_dict["first_name"].append(player.first_name)
            player_dict["birth_date"].append(player.birth_date)
            player_dict["gender"].append(player.gender)
            player_dict["ranking"].append(player.ranking)
            player_dict["points"].append(player.point)
        return self

    def sort_player_by_rank(self):
        player_list_dict = []
        for player in self.players:
            player_list_dict.append(
                player.player_object_to_dict()
            )
        player_list_dict = sorted(player_list_dict, key=itemgetter("ranking"))
        i = 0
        for player in self.players:
            player.player_dict_to_object_(player_list_dict[i])
            i +=1
        return self.players

    def sort_player_by_points(self):
        player_list_dict = []
        for player in self.players:
            player_list_dict.append(
                player.player_object_to_dict()
            )
        player_list_dict = sorted(player_list_dict, key=itemgetter("point"))
        i = 0
        for player in self.players:
            player.player_dict_to_object_(player_list_dict[i])
            i += 1
        return self.players

    def adding_score_to_players_instance_from_match(self, match_list):
        #transform the tuple from match into list to manipulate him
        match_list_list=[]
        for match in match_list:
            current = list(match)
            match_list_list.append(current)
        i=0
        #store on the new list string value to manipulate the index
        for match in match_list_list:
            match[i] = str(match[i])
            i+=1
        index = match_list_list[0].index("cicconi silvio")
        print(f'coucou voici l index {index}')
        return self.players