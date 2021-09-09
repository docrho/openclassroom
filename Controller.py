import Model
import View
import json
from Match import Match
from Player import Player
from Tournament import Tournament
v = View.Views()
db = Model.DbManager()

# function######


def home():
    v.load_page("home")
    response = str(input())
    return response


# starting app####


while True:

    responsemenu = home()
    if responsemenu == "0":  # To quit
        break

    elif responsemenu == "1":  # load tournament

        v.load_page('display_tournament')

    elif responsemenu == "2":  # create new tournament
        # displaying all player on the console
        v.load_page("display_all_players", db.get_all_players())
        # return the 8 player number prompt taht we want to select
        player_id_list = v.load_page("create_tournament_players")
        all_id = db.get_all_players_id()
        # checking up if the id exist on all_id list
        id_exist = db.player_id_checking(player_id_list)
        if id_exist:
            player_selected = []
            # getting all player from database with doc_id
            for player_id in player_id_list:
                # adding on player selected each player from id
                player_selected.append(db.players.get(doc_id=int(player_id)))
            # serialize player to put them on database
            player_selected = json.dumps(player_selected)
            # calling view for ask tournament name prompt ....
            tournament_info = v.create_tournament()
            # creating tournament with tournament Class
            tournament = Tournament(
                tournament_info['name'], tournament_info['place'],
                tournament_info['date'], "4", player_selected, tournament_info['time'], tournament_info['description']
            )
            # store tournament on database
            db.store_tournament(tournament)
        else:
            v.load_page("error","player_id")

    elif responsemenu == "3":  # add a player on Player database

        # init a player that we will send it to view
        player = Player()
        player = v.load_page("add_player_view", player)
        # Taking all player data to compare them with current player, its for avoiding double
        all_players_data = db.players.all()
        # add_player return True if there is no double
        added = db.add_player(all_players_data, player)
        # load a page to print succeffull or not
        v.load_page("player_successfully_added_or_not", added, player)

    elif responsemenu == "4":  # remove a player on Player database
        player_to_remove = v.remove_player()
        # player contain a list that contain lastname and birth_date from view
        if db.remove_players(player_to_remove[0], player_to_remove[1]):
            v.load_page("success","player_removed")
        else:
            v.load_page("error","player_not_removed")


    elif responsemenu == "5":  # list all players from Player database

        v.display_all_players(db.list_all_players())

    elif responsemenu == "6":  # Remove a tournament
        if db.remove_tournament(v.response_input()):
            v.load_page("success","tournament_removed")
        else:
            v.load_page("error","tournament_not_removed")

    elif responsemenu == "7":  # List all tournament
        v.load_page("list_tournament", db.tournament.all())

    elif responsemenu == "8":  # update a tournament
        tournament_id = int(v.load_page("_update_tournament_menu_prompt"))  # store the response on variable tournament_id
        tournament = []  # the variable where to store the tournament
        if db.tournament_id_check(tournament_id):  # checking if the tournament id exist
            tournament.append(db.tournament.get(doc_id=tournament_id))  # add to the variable all tournament matched the query
            v.load_page("list_tournament", tournament)  # display the tournament selected

            while responsemenu != "6":  # condition to exit the loop
                v.load_page("update_tournament_menu")
                responsemenu = v.basic_input()
                if responsemenu == "1":  # change name condition
                    db.update_tournament("name", tournament_id, v.load_page("change_tournament_prompt"))  # passing the id prompted to the method by tournament_id
                if responsemenu == "2":
                    db.update_tournament("place", tournament_id, v.load_page("change_tournament_prompt"))  # passing the id prompted to the method by tournament_id
                if responsemenu == "3":
                    db.update_tournament("date", tournament_id, v.load_page("change_tournament_prompt"))  # passing the id prompted to the method by tournament_id
                if responsemenu == "4":
                    db.update_tournament("description", tournament_id, v.load_page("change_tournament_prompt"))  # passing the id prompted to the method by tournament_id
                if responsemenu == "5":
                    db.remove_tournament(tournament_id)

        else:
            v.load_page("error", "tournament_id")
    elif responsemenu == "9":  # Match
        v.load_page("list_tournament", db.tournament.all())
        tournament_id = int(v.load_page("_update_tournament_menu_prompt"))  # store the response on variable tournament_id
        tournaments = []  # the variable where to store the tournament
        if db.tournament_id_check(tournament_id):  # checking if the tournament id exist
            # add to the variable all tournament who matched the query
            tournaments.append(db.tournament.get(doc_id=tournament_id))
            v.load_page("list_tournament", tournaments)  # display the tournament selected
            # extract players from tournament
            tournament_players_list = db.get_all_players_in_tournament(tournament_id)
            match = Match()
            match.print_players_list(tournament_players_list)
        else:
            v.load_page("error","tournament_id")
