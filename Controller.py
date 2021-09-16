from Db import DbManager
import View
import json
from Match import Match
from Player import Player
from Tournament import Tournament
player=Player()
v = View.Views()
db = DbManager()

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
        all_players_data = db.players.all()
        player_list = []
        for player_data in all_players_data:
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

        v.load_page("display_all_players", player_list)
        # return the 8 player number prompt taht we want to select
        player_id_list = v.load_page("create_tournament_players")
        #all_id = player.get_all_players_id(all_players_data)
        # checking up if the id exist on all_id list
        id_exist = player.player_id_checking(player_id_list, all_players_data)
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
                tournament_info['date'], "4", player_selected,
                tournament_info['time'], tournament_info['description'],
            )
            # store tournament on database
            db.store_tournament(tournament)
        else:
            v.load_page("error", "player_id")

    elif responsemenu == "3":  # add a player on Player database

        # init a player that we will send it to view
        player_prompt = Player()
        player_prompt = v.load_page("add_player_view", player_prompt)
        # Taking all player data to compare them with current player,
        # its for avoiding double
        all_players_data = db.players.all()
        player_list = []
        # instancing the deserialized data
        for player_data in all_players_data:

            player_list.append(Player(
                player_data["lastname"],
                player_data["first_name"],
                player_data["birth_date"],
                player_data["gender"],
                player_data["ranking"],
                player_data["points"],
                                      )
                               )
            
        # add_player return True if there is no double
        added = db.add_player(player_list, player_prompt)
        # load a page to print succeffull or not
        v.load_page("player_successfully_added_or_not", added, player_prompt)

    elif responsemenu == "4":  # remove a player on Player database
        player_to_remove = v.remove_player()
        # player contain a list that contain lastname and birth_date from view
        if db.remove_players(player_to_remove[0], player_to_remove[1]):
            v.load_page("success", "player_removed")
        else:
            v.load_page("error", "player_not_removed")

    elif responsemenu == "5":  # list all players from Player database
        player = Player()
        player_data = db.players.all()
        player_list = player.list_all_players(player_data)
        v.display_all_players(player_list)

    elif responsemenu == "6":  # Remove a tournament
        if db.remove_tournament(v.response_input()):
            v.load_page("success", "tournament_removed")
        else:
            v.load_page("error", "tournament_not_removed")

    elif responsemenu == "7":  # List all tournament
        tournament_list = []
        all_tournament = db.tournament.all()

        for tournament_data in all_tournament:
            tournament_list.append(
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
        v.load_page("list_tournament", tournament_list)

    elif responsemenu == "8":  # update a tournament
        # store the response on variable tournament_id
        tournament_id = int(v.load_page("_update_tournament_menu_prompt"))
        tournament = []  # the variable where to store the tournament
        # checking if the tournament id exist
        if db.tournament_id_check(tournament_id):
            # add to the variable all tournament matched the query
            tournament_data = db.tournament.get(doc_id=tournament_id)
            tournament.append(
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
            # display the tournament selected
            v.load_page("list_tournament", tournament)

            while responsemenu != "6":  # condition to exit the loop
                v.load_page("update_tournament_menu")
                responsemenu = v.basic_input()
                if responsemenu == "1":  # change name condition
                    # passing the id prompted to the method by tournament_id
                    db.update_tournament(
                        "name", tournament_id,
                        v.load_page("change_tournament_prompt"))
                if responsemenu == "2":
                    # passing the id prompted to the method by tournament_id
                    db.update_tournament(
                        "place", tournament_id,
                        v.load_page("change_tournament_prompt"))
                if responsemenu == "3":
                    # passing the id prompted to the method by tournament_id
                    db.update_tournament(
                        "date", tournament_id,
                        v.load_page("change_tournament_prompt"))
                if responsemenu == "4":
                    # passing the id prompted to the method by tournament_id
                    db.update_tournament(
                        "description", tournament_id,
                        v.load_page("change_tournament_prompt"))
                if responsemenu == "5":
                    db.remove_tournament(tournament_id)

        else:
            v.load_page("error", "tournament_id")
    elif responsemenu == "9":  # Match
        v.load_page("list_tournament", db.tournament.all())
        # store the response on variable tournament_id
        tournament_id = int(v.load_page("_update_tournament_menu_prompt"))
        tournaments = []  # the variable where to store the tournament
        # checking if the tournament id exist
        if db.tournament_id_check(tournament_id):
            # add to the variable all tournament who matched the query
            tournaments.append(db.tournament.get(doc_id=tournament_id))
            # display the tournament selected
            v.load_page("list_tournament", tournaments)
            # extract players from tournament
            tournament_players_list = db.get_all_players_in_tournament(
                tournament_id)
            match = Match()
            first_match = match.first_match(tournament_players_list)
            print(first_match[0]["players"][0])
        else:
            v.load_page("error", "tournament_id")
