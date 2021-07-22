from tinydb import TinyDB, Query


class Player(TinyDB):

    def __init__(self, last_name, first_name, birth_date, gender, ranking):
        self.lastname = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.db = TinyDB("db.json")

    def store(self):
        self.db.insert({
            "type":"player","lastname":self.lastname,"first_name":self.first_name,
            "birth_date":self.birth_date, "gender":self.gender, "ranking":self.ranking
        })

    def player_display (self,player):
        print(player.lastname)

class DbManager(TinyDB):

    def __init__(self):
        self.db = TinyDB("db.json")
        self.players = self.db.table("players")
        self.tournament=self.db.table('tournament')
    def storePlayer(self,player):
        self.players.insert({
            "type": "player", "lastname": player.lastname, "first_name": player.first_name,
            "birth_date": player.birth_date, "gender": player.gender, "ranking": player.ranking
        })

    def storeTournament(self,tournament):
        self.tournament.insert({
            "type": "player", "name": tournament.name, "place": tournament.place,
            "date": tournament.date, "nb_turn": tournament.nb_turn ,"players": tournament.players,
            "time": tournament.time, "description": tournament.description, "tournament_id": tournament.tournament_id
        })

class Round():
    def __init__(self,player1,player2):
        self.player1=player1
        self.player2=player2

    def winner(self):
        print("type 1 if "+self.player1.lastname +"have win, otherwise type 2")
        whowin=input()
        return print("the player "+whowin+"have winned")


class Tournament():
    def __init__(self,name,place,date,nb_turn,players,time,description,tournament_id):
        self.name=name
        self.place=place
        self.date=date
        self.nb_turn=nb_turn
        self.players=players
        self.time=time
        self.description=description
        self.tournament_id=tournament_id


