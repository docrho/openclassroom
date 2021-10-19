from Db import DbManager
import View
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
        tournament = Tournament()
        player = Player()
        # store the response on variable tournament_id

        tournament_id = int(v.load_page("_update_tournament_menu_prompt"))
        # checking if the tournament id exist
        if tournament.tournament_id_checking(tournament_id):
            # adding tournament from database on tournament instance
            tournament.tournament_instance(tournament.get_tournament_by_id(
                tournament_id)
            )
            tournament_players_list = tournament.players
            v.load_page("list_tournament", tournament)
            #instancing player from tournament.players
            tournament.players = player.player_instance(tournament.players)
            while True:
                v.display_all_players_from_tournament(tournament.players)
                responsemenu = v.start_match()
                if responsemenu == '0':
                    break
                else:
                    match = Match(list(tournament_players_list))
                    first_match = match.first_match()
                    print(first_match)

                ###should tournament.start_match





    elif responsemenu == "2":  # create new tournament
        tournament = Tournament()
        player = Player()
        # store on attribute all player from database
        list_players = Player.list_all_players()
        # we are displaying all player ,like this we can choose them by id
        v.load_page("display_all_players", list_players)
        # return the 8 player number prompt that we want to select
        player_id_list = v.load_page("create_tournament_players")
        # checking up if the id prompted exist
        if Player.players_id_checking(player_id_list):
            #this method add player and serialize them
            #verifier les id dans append, la methode static
            Player.append_player_from_id(player_id_list)
            # calling view for ask tournament name prompt ....
            tournament_info = v.create_tournament()
            # creating tournament with tournament method
            tournament.add_tournament_info(tournament_info,
                                           Player.serialized_players_list)
            # store tournament on database
            db.store_tournament(tournament)
        else:
            v.load_page("error", "player_id")

    elif responsemenu == "3":  # add a player on Player database
        # init a player that we will send it to view
        player_prompt = v.load_page("add_player_view", Player())
        # Taking all player data to compare them with current player,
        # its for avoiding double
        # instancing the deserialized data
        list_all_players = Player.list_all_players()#static
        # add_player return True if there is no double on database
        added_bol = db.add_player(list_all_players, player_prompt)
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
        v.display_all_players(Player().list_all_players())

    elif responsemenu == "6":  # Remove a tournament
        tournament = Tournament() #static needed
        # le remove doit fonctionner que après une instance de tournois
        #ensuite remove on ne devrai pas specifier l id quand on remove
        #car c est déja instancié
        #remove from id
        ###########################
        if tournament.remove_tournament(v.response_input()):
            v.load_page("success", "tournament_removed")
        else:
            v.load_page("error", "tournament_not_removed")

    elif responsemenu == "7":  # List all tournament
        tournament = Tournament()
        tournament.list_all_tournament()#static
        v.load_page("list_tournament", tournament.all_tournament_list)

    elif responsemenu == "8":  # update a tournament
        tournament = Tournament()
        # store the response on variable tournament_id
        tournament_id = int(v.load_page("_update_tournament_menu_prompt"))
        # checking if the tournament id exist
        if tournament.tournament_id_checking(tournament_id):
            # adding tournament from database on tournament instance
            tournament.tournament_instance(tournament.get_tournament_by_id(
                tournament_id)
            )
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
                    tournament.remove_tournament(tournament_id)

        else:
            v.load_page("error", "tournament_id")
    elif responsemenu == "9":  # Match
        tournament = Tournament()
        tournament._all_tournament_instance()

        v.load_page("list_tournament", tournament.all_tournament_list)
        # store the response on variable tournament_id
        tournament_id = int(v.load_page("_update_tournament_menu_prompt"))
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
            tournament_players_list = tournament.tournament_list[0].players
            match = Match()
            first_match = match.first_match(tournament_players_list)
            print(first_match)
        else:
            v.load_page("error", "tournament_id")
