import Model
import View
import json
import Match
from Player import Player
v = View.Views()
db = Model.DbManager()

###function######

def home():
    v.load_page("home")
    response = str(input())
    return response


####starting app####


while True:

    responsemenu = home()
    if responsemenu == "0":# To quit
        break
    elif responsemenu == "1": #load tournament
        v.load_page('display_tournament')
    elif responsemenu == "2": #  create new tournament

        v.load_page("create_tournament")
        ###creating the tournament with good id#####
        players_serialized = db.players.all()

        players_serialized = json.dumps(players_serialized)
        tournament = Model.Tournament("de Noel", "Paris", "25/12/2021", "4", players_serialized, "2h",
                                      "c est le fameux tournois de noel")
        ####store and remove####
        db.store_tournament(tournament)
        # db.remove_tournament(2)
        #####empy player storage#####

    elif responsemenu == "3": # add a player on Player database
        ### init a player that we will send it to view
        player = Player()
        player = v.load_page("add_player_view",player)
        #Taking all player data to compare them with current player, its for avoiding double
        all_players_data = db.players.all()
        # add_player return True if there is no double
        added = db.add_player(all_players_data, player)
        if added:

            print(f"The player {player.lastname} {player.first_name} was added !!!\n")
        else:
            print("Player already exist, so not added")

    elif responsemenu == "4":#remove a player on database
        db.remove_players("first_name", "romano")

    elif responsemenu == "5":# list all players from Player database
        v.display_all_players(db.list_all_players())

    elif responsemenu == "6": # Remove a tournament
        db.remove_tournament(v.response_input())

    elif responsemenu == "7":#List all tournament
        v.load_page("list_tournament", db.tournament.all())

    elif responsemenu == "8":# update a tournament
        tournament_id = int(v._update_tournament_menu_prompt()) #store the response on variable tournament_id
        tournament= [] #the variable where to store the tournament
        if db.tournament_id_check(tournament_id): # checking if the tournament id exist
            tournament.append(db.tournament.get(doc_id=tournament_id)) # add to the variable all tournament matched the query
            v.load_page("list_tournament",tournament) #display the tournament selected

            while responsemenu != "6": # condition to exit the loop
                v.load_page("update_tournament_menu")
                responsemenu = v.basic_input()
                if responsemenu == "1": # change name condition
                    db.update_tournament("name",tournament_id,v.load_page("change_tournament_prompt"))#passing the id prompted to the method by tournament_id
                if responsemenu == "2":
                    db.update_tournament("place",tournament_id,v.load_page("change_tournament_prompt"))#passing the id prompted to the method by tournament_id
                if responsemenu == "3":
                    db.update_tournament("date",tournament_id,v.load_page("change_tournament_prompt"))#passing the id prompted to the method by tournament_id
                if responsemenu == "4":
                    db.update_tournament("description",tournament_id,v.load_page("change_tournament_prompt"))#passing the id prompted to the method by tournament_id
                if responsemenu == "5":
                    db.remove_tournament(tournament_id)

        else:
            v.load_page("error", "tournament_id")
    elif responsemenu == "9":# Match
        v.load_page("list_tournament", db.tournament.all())
        tournament_id = int(v._update_tournament_menu_prompt())  # store the response on variable tournament_id
        tournaments = []  # the variable where to store the tournament
        if db.tournament_id_check(tournament_id): # checking if the tournament id exist
            # add to the variable all tournament who matched the query
            tournaments.append(db.tournament.get(doc_id=tournament_id))
            v.load_page("list_tournament",tournaments) #display the tournament selected
            ###extraire les player du tournament
            player_list=[]
            player_deserial=[]
            for tournament in tournaments:
                player_list.append(tournament["players"])
            for player in player_list: #deserialiser
                player_deserial.append(json.loads(player))
                print(player_deserial[0][0])

