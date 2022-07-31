class Club(object):

    def __init__(self, name, code, country):
        self.name = name
        self.code = code
        self.country = country


import json


def get_all_clubs():
    with open("english_clubs.json", "r", encoding="utf-8") as stream:
        data = json.load(stream)
        teams = []
        for team in data['clubs']:
            club = Club(team['name'], team['code'], team['country'])
            teams.append(club)

    return teams
