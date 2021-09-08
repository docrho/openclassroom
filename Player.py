class Player:

    def __init__(self, last_name="", first_name="", birth_date="", gender="", ranking=""):
        self.lastname = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
    def __str__(self):
        return self.lastname