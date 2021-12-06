from Db import DbManager
import View
import json
from Match import Match
from Player import Player
from Tournament import Tournament

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
        tournament = Tournament()
        # store on attribute all player from database
        list_players = player.list_all_players()
        # we are displaying all player ,like this we can choose them by id
        v.load_page("display_all_players", list_players)
        # return the 8 player number prompt that we want to select
        player_id_list = v.load_page("create_tournament_players")
        # checking up if the id prompted exist
        if player.players_id_checking(player_id_list):
            #this method add player and serialize them
            player.append_player_from_id(player_id_list)
            # calling view for ask tournament name prompt ....
            tournament_info = v.create_tournament()
            # creating tournament with tournament method
            tournament.add_tournament_info(tournament_info,
                                           player.serialized_players_list)
            # store tournament on database
            db.store_tournament(tournament)
        else:
            v.load_page("error", "player_id")

    elif responsemenu == "3":  # add a player on Player database
        player = Player()
        # init a player that we will send it to view
        player_prompt = v.load_page("add_player_view", Player())
        # Taking all player data to compare them with current player,
        # its for avoiding double
        # instancing the deserialized data
        player.list_all_players()
        # add_player return True if there is no double on database
        added_bol = db.add_player(player.all_players, player_prompt)
        # load a page to print successfull or not
        v.load_page("player_successfully_added_or_not",
                    added_bol,
                    player_prompt
                    )

    elif responsemenu == "4":  # remove a player on Player database
        player_to_remove = v.remove_player(Player())
        # player contain a list that contain lastname and birth_date from view
        if db.remove_players(player_to_remove.lastname,#player.remove
                             player_to_remove.birth_date):
            v.load_page("success", "player_removed")
        else:
            v.load_page("error", "player_not_removed")

    elif responsemenu == "5":  # list all players from Player database
        player = Player()
        player.list_all_players()
        v.display_all_players(player.all_players)

    elif responsemenu == "6":  # Remove a tournament
        if tournament.remove_tournament(v.response_input()):
            v.load_page("success", "tournament_removed")
        else:
            v.load_page("error", "tournament_not_removed")

    elif responsemenu == "7":  # List all tournament
        tournament = Tournament()
        tournament.list_all_tournament()
        v.load_page("list_tournament", tournament.all_tournament_list)

    elif responsemenu == "8":  # update a tournament
        # store the response on variable tournament_id
        tournament_id = int(v.load_page("_update_tournament_menu_prompt"))
        # checking if the tournament id exist

        ## faire tout en une etape
        if db.tournament_id_check(tournament_id): # a mettre dans tournament
            # adding tournament from database on tournament instance
            tournament.tournament_instance(db.tournament.get(
                doc_id=tournament_id))
            v.load_page("list_tournament", tournament.tournament_list)
        #########jusque ici########
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
        tournament = Tournament()
        ##instancie tout les tournois
        tournament.all_tournament_instance(db.tournament.all())

        v.load_page("list_tournament", tournament.tournament_list)
        # store the response on variable tournament_id
        tournament_id = int(v.load_page("_update_tournament_menu_prompt"))

        # checking if the tournament id exist
        ########

        ######faire une seule etape cela doit rester caché#####
        if db.tournament_id_check(tournament_id):
            # add to the variable the tournament who matched the query
            tournament_data = db.tournament.get(doc_id=tournament_id)
            # creating instance
        ########### ici########

            tournament.tournament_instance(tournament_data)
            v.load_page("list_tournament", tournament.tournament_list)
            # extract players from tournament
            # attention trouver le bug
            tournament_players_list = tournament.players
            match = Match()
            print(tournament.players)
            first_match = match.first_match2(tournament.players)
            print(first_match)
        else:
            v.load_page("error", "tournament_id")
