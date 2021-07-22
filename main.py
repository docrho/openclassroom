from Model import Player, DbManager, Tournament, Round
from rich.console import Console
from tinydb import Query
from tinydb import where
import json

console=Console()
#player = Player("cicconi","romano","05/03/1990","male","2000")
#player.store()
#player2 = Player("Blanquet","nicolas","07/07/1993","male","2300")
#player2.store()
db=DbManager()
#roundenquestion=Round(player,player2)
#roundenquestion.winner()

console.print("Bonjours tapez 1 pour load un tournoi sinon appuyer sur une autre touche pour creer")
menuresponse=input()

if (menuresponse==1):
    print('coucou')

else :
    console.print("[bold white on green]:beer:welcome to the tournament, how many player did you want?")
    nb_of_player=2
    int(nb_of_player)
    console.print("okey you want "+ str(nb_of_player )+"players")
    i = 0
    players=[]
    while(i < int(nb_of_player)):
        console.print("type the lastname,firstname,date of birth,gender and ranking")
        players.append(Player(input(),input(),input(),input(),input()))

        i +=1
        if (i == int(nb_of_player)):
            for player in players:
                db.storePlayer(player)
    #####creation de joueur fini, loadon les joueurs dans une variable pour les randomiser ######
    ####serialisation et maintenant deserialisation####

    coucou=db.players.all()
    coucou=json.dumps(coucou) #adding double quote
    coucou=json.loads(coucou)#deserialize
    #print(coucou[0]["lastname"])
    for coucoux in coucou:
        print(coucoux["first_name"])

    ####creation tournament
    def unique_id_creator(all_tournament):
        id_dic=[]
        id=all_tournament
        id= json.dumps(all_tournament)
        id= json.loads(all_tournament)
        for all_tournament in all_tournamentl:
            id_dic.append(all_tournament["tournament_id"])
        return id_dic

    id_i=[]    ##init iterator
    tournament_id_iterated = db.tournament.all()
    tournament_id_iterated = json.dumps(tournament_id_iterated)
    tournament_id_iterated = json.loads(tournament_id_iterated)
    for tournament_id_iterated in tournament_id_iterated:
        id_i.append(tournament_id_iterated["tournament_id"])

    print(id_i)
    if not id_i:
        id_i.append(1)
    #####on peut maintenant creer un tournois avec un id unique##suffi de rajouter les option input pour la creation##
    tournament=Tournament("de Noel","Paris","25/12/2021","4",coucoux,"2h","c est le fameux tournois de noel",len(id_i)+1)
    db.storeTournament(tournament)
    print('le dernier tournament est le numero '+ str(id_i[-1]+1))

