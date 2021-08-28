import Model
import View
import json


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
    if responsemenu == "0":
        break
    elif responsemenu == "1":
        v.load_page('display_tournament')
    elif responsemenu == "2":

        v.load_page("create_tournament")
        ####tournament id creator######
        ##init iterator
        id_i = []
        tournament_id_iterated = db.tournament.all()
        tournament_id_iterated = json.dumps(tournament_id_iterated)
        tournament_id_iterated = json.loads(tournament_id_iterated)

        for tournament_id_iterated in tournament_id_iterated:
            id_i.append(tournament_id_iterated["tournament_id"])
        ###creating the tournament with good id#####
        players_serialized = db.players.all()

        players_serialized = json.dumps(players_serialized)
        if not id_i:
            max_value = 0
        else:
            max_value = max(id_i)
        tournament = Model.Tournament("de Noel", "Paris", "25/12/2021", "4", players_serialized, "2h",
                                      "c est le fameux tournois de noel", max_value + 1)
        ####store and remove####
        db.store_tournament(tournament)
        # db.remove_tournament(2)
        #####empy player storage#####

    elif responsemenu == "3":
        player = Model.Player("cicconi", "romano", "05/03/1990", "male", "2000")
        all_players_data = db.players.all()

        added = db.add_player(all_players_data, player)
        print(added)
    elif responsemenu == "4":
        db.remove_players("first_name", "romano")
    elif responsemenu == "5":
        v.display_all_players(db.list_all_players())
    elif responsemenu == "6":
        db.remove_tournament(v.response_input())
    elif responsemenu == "7":
        v.load_page("list_tournament", db.tournament.all())
    elif responsemenu == "8":
        tournament_id = int(v._update_tournament_menu_prompt()) #store the response on variable tournament_id
        tournament= [] #the variable where to store the tournament
        if db.tournament_id_check(tournament_id): # checking if the tournament id exist
            tournament.append(db.tournament.get(doc_id=tournament_id)) # add to the variable all tournament matched the query
            v.load_page("list_tournament",tournament) #display the tournament selected

            while responsemenu != "6": # condition to exit the loop
                v.load_page("update_tournament_menu")
                responsemenu = v.basic_input()
                if responsemenu == "1": # change name condition
                    db.update_tournament(tournament_id,v.load_page("change_tournament_prompt"))#passing the id prompted to the method by tournament_id






        else:
            v.load_page("error", "tournament_id")
