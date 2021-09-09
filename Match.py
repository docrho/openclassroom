import Player
import json
from operator import itemgetter
class Match:
    def print_players_list(self, players_list: list):
        print(players_list)

        return players_list

    def first_match(self, players_list: list):
        sorted_list =  sorted(players_list, key=itemgetter("ranking"))
        players_match = {}
        match = []
        i = 0
        while i <= 3:
            players_match["players"] = [sorted_list[i], sorted_list[i+4]]
            players_match["score"] = ["0","0"]
            match.append(players_match)
            i += 1
        print(match[0]["score"])
        return match

    def match_list_generator(self):
        return match_list
    def tour(self):
        print()
