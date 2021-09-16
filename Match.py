from operator import itemgetter


class Match:

    def first_match(self, players_list: list):
        players_list_serialized = []
        for players in players_list:
            players_list_serialized.append({
                "type": "player",
                "lastname": players.lastname,
                "first_name": players.first_name,
                "birth_date": players.birth_date,
                "gender": players.gender,
                "ranking": players.ranking,
                "points": players.point,
            })
        sorted_list = sorted(players_list_serialized, key=itemgetter("ranking"))
        players_match = {}
        match = []
        i = 0
        while i <= 3:
            players_match["players"] = [sorted_list[i], sorted_list[i+4]]
            players_match["score"] = ["0", "0"]
            match.append(players_match)
            i += 1
        return match

    def match_list_generator(self, match_list):

        return match_list

    def tour(self):
        print()
