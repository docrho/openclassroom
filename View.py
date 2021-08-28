

class Views():
    def success(self,success):
        if success == "player_added":
            print('Players added successfuly ')
    def display_all_players(self,all_players):
        for players in all_players:
            print(players['lastname'])
    def _error(self,error_name):
        if "player_name_exist" in error_name:
            print("le player name already exist\n")

        if "tournament_id" in error_name:
            print("The tournament id was not found!!\n")
    def response_input (self):
        print('tapez le numero du tournois a supprimer')
        return input()
    def _base_menu(self):
        print("Hi, Welcome to tournament chess app!\nType "
              "\n1 to load a tournament "
              "\n2 to create new tournament "
              "\n3 to add a player "
              "\n4 to remove a player "
              "\n5 to list all players "
              "\n6 to remove a tournament "
              "\n7 to list all tournaments "
              "\n8 update tournament "
              "\n9 to select a player by his id "
              "\n0 to quit the app")
    def _tournaments_displays(self):
        print("ont load le tournament")
    def list_tournament(self,tournaments):
        for tournament in tournaments:

            for tour in tournament:

                print(
                "tournament name :: "+tour['name'],
                "\ntournament place :: "+tour["place"],
                "\ntournament date :: "+tour["date"],
                "\n tournament id :: "+str(tour.doc_id),
                "\n----------------------------------------"
                )

    def _create_tournament(self):
        print("creation du tournoi")

    def load_page(self, page_name: str, *args, **kwargs):
        if page_name == "home":
            self._base_menu()
        elif page_name == "display_tournament":
            self._tournaments_displays()
        elif page_name == "create_tournament":
            self._create_tournament()
        elif page_name == "list_tournament":
            self.list_tournament(args)
        elif page_name == "error":
            self._error(args)
