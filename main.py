from Model import Player,Round,DbManager,Tournament
from Controller import Controller
from View import Views
from rich.console import Console
from tinydb import where
import json

console=Console()

###########test#########
#player = Player("cicconi","romano","05/03/1990","male","2000")
#player.store()
#player2 = Player("Blanquet","nicolas","07/07/1993","male","2300")
#player2.store()
###############test#############


db=controller.db ###init database from controller

controller.view.base_menu()

choice=input() ####choose what to do

player=controller.create_player("cicconi","romano","05/03/1990","male","2000") #create new player on player instance
db.storePlayer(player) ####store player ## a faire creer un player le storer dans la databse avec le numero du tournoi cree
player_serialized=db.players.all()###store tout les players # afaire prendre tout les player du numero du tournoi pour fabriquer le tournoi avec
player_serialized=json.dumps(player_serialized)


id_i=[]
id_i=controller.unique_id_creator(db.tournament.all())##init iterator
tournament=controller.create_tournament(id_i,player_serialized)
db.storeTournament(tournament)



#roundenquestion=Round(player,player2)
#roundenquestion.winner()

#############function###############
#console.print("[bold white on green]:beer:welcome to the tournament, how many player did you want?")
#nb_of_player=2
#int(nb_of_player)
#console.print("okey you want "+ str(nb_of_player )+"players")
#i = 0
#players=[]
#while(i < int(nb_of_player)):
# #   console.print("type the lastname,firstname,date of birth,gender and ranking")
#    players.append(Player(input(),input(),input(),input(),input()))
#
#    i +=1
 #   if (i == int(nb_of_player)):
#        for player in players:
 #           db.storePlayer(player)
#####creation de joueur fini, loadon les joueurs dans une variable pour les randomiser ######
####serialisation et maintenant deserialisation####
