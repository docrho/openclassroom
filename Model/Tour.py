from Model.Match2 import Match

class Tour:
    def __init__(self):
        self.match_list =[]
        self.name = ""
        self.start_time = ""
        self.end_time = ""

    #adding result prompt from view to all match from match list
    def add_score_to_match(self, score_from_view: list):
        for match in self.match_list:
            match.score_joueur1 = score_from_view[0]
            match.score_joueur2 = score_from_view[1]

