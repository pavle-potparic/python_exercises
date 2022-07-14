
# TODO: 1. Refactor code from english league. Create new file and send all methods in this file. Import this file, and call this methods in english_league and spanish league python files.
# TODO: This file should be named as footbal_league_interface.py. Renama some name of methods and params to get understandable code.
# TODO: 2. Write english_final_table_2018.json and spanish.final_table_2018.json files. Json should contain all data that you have already printed.
# TODO: 3. All methods should have doc, and defined type of params and return values
# Example of Json file:
# [
# {"position": 1,
#  "team": "Manchester City FC",
#  "matches":{
#      "played": 38,
#      "won": 32,
#      "draw": 4,
#      "lose": 2
#   },
#  "scores":{
#      "for": 106,
#      "against": 27,
#      "goal_difference": 79
#   },
#  "points": 100
# }
# ]


import football_leagues_interface as football
import json

english_teams = "english_clubs.json"
english_matches = "english_matches.json"


# with open(english_teams, "r", encoding="utf-8") as stream_clubs, open(english_matches) as stream_matches:
#     data_teams = json.load(stream_clubs)
#     teams = []
#     for club in data_teams['clubs']:
#         teams.append(club['name'])
#
#     print(teams)





def get_from_dict_by_key(dict, key):
    return dict[key]


def get_name_of_teams(all_clubs, key):
    teams = []
    for club in all_clubs:
        teams.append(club[key])
    return teams


def prepare_teams_score_dict(team_names):
    """
    Napravio sam metodu koja treba da napravi recnik u kome ce kljuc biti ime tima, a vrednost njegovi rezultati
    smesteni u listu
    key = team name
    value[0] = played matches
    value[1] = won
    value[2] = draw
    value[3] = loose
    value[4] = for goals
    value[5] = against goals
    value[6] = goal difference
    value[7] = points
    :param team_names: je parametar kojim dobijam listu svih timova koju pretvaram u recnik
    :return: metoda vraca recnik timova i njihovih rezultata koji su na nuli
    """

    team_dict = {}
    for key in team_names:
        team_dict[key] = [0, 0, 0, 0, 0, 0, 0, 0]
    return team_dict


def get_list_of_matches(match_list):
    list_of_matches = []
    for match in match_list:
        list_of_matches.append(match['matches'])
    return list_of_matches


def get_points_of_one_team(list_of_matches, list_of_results):
    # matchday = list_of_matches[0]

    for team in team_names:
        for matchday in list_of_matches:
            for match in matchday:
                team1 = match['team1']
                team2 = match['team2']
                scores = match['score']['ft']
                team1_score = scores[0]
                team2_score = scores[1]

                if team == team1:
                    list_of_results[team1][0] += 1
                    if team1_score == team2_score:
                        # point += 1
                        list_of_results[team1][2] += 1
                        list_of_results[team1][7] += 1
                    elif team1_score > team2_score:
                        # point += 3
                        list_of_results[team1][1] += 1
                        list_of_results[team1][7] += 3
                    else:
                        list_of_results[team1][3] += 1
                    list_of_results[team1][4] += team1_score
                    list_of_results[team1][5] += team2_score

                elif team == team2:
                    list_of_results[team2][0] += 1
                    if team2_score == team1_score:
                        # point += 1
                        list_of_results[team2][7] += 1
                        list_of_results[team2][2] += 1
                    elif team2_score > team1_score:
                        # point += 3
                        list_of_results[team2][1] += 1
                        list_of_results[team2][7] += 3
                    else:
                        list_of_results[team2][3] += 1
                    list_of_results[team2][4] += team2_score
                    list_of_results[team2][5] += team1_score

        list_of_results[team][6] = list_of_results[team][4] - list_of_results[team][5]

    # print("Team", team, "points:", point, "For goals:", for_goals, "Against: ", against)
    return list_of_results


def pravljenje_tabele(dict_timova_i_njihovih_rezultata):
    lista_timova_i_njihovih_rezultata = []
    for key, value in dict_timova_i_njihovih_rezultata.items():
        value.append(key)
        lista_timova_i_njihovih_rezultata.append(value)
    broj_ponavljanja_while = 1
    while True:
        if broj_ponavljanja_while < 20:
            for index in range(0, len(lista_timova_i_njihovih_rezultata)):
                if index < len(lista_timova_i_njihovih_rezultata) - 1:
                    if lista_timova_i_njihovih_rezultata[index][7] < lista_timova_i_njihovih_rezultata[index + 1][7]:
                        lista_timova_i_njihovih_rezultata[index], lista_timova_i_njihovih_rezultata[index + 1] = \
                            lista_timova_i_njihovih_rezultata[index + 1], lista_timova_i_njihovih_rezultata[index]
                    if lista_timova_i_njihovih_rezultata[index][7] == lista_timova_i_njihovih_rezultata[index + 1][7]:
                        if lista_timova_i_njihovih_rezultata[index][6] < lista_timova_i_njihovih_rezultata[index + 1][
                            6]:
                            lista_timova_i_njihovih_rezultata[index], lista_timova_i_njihovih_rezultata[index + 1] = \
                                lista_timova_i_njihovih_rezultata[index + 1], lista_timova_i_njihovih_rezultata[index]

            broj_ponavljanja_while += 1
        else:
            break

    return lista_timova_i_njihovih_rezultata


data_teams = football.get_data(english_teams)
all_clubs = get_from_dict_by_key(data_teams, "clubs")
team_names = get_name_of_teams(all_clubs, 'name')
prepare_teams_dict = prepare_teams_score_dict(team_names)

data_matches = football.get_data(english_matches)
match_rounds = get_from_dict_by_key(data_matches, "rounds")
list_of_matches = get_list_of_matches(match_rounds)

timovi_i_nihovi_rezultati = get_points_of_one_team(list_of_matches, prepare_teams_dict)
tabela = pravljenje_tabele(timovi_i_nihovi_rezultati)


def pravljenje_dobijenih_rezultata_dict(dict_tabele):
    tabela_timova_i_njihovih_rezultata = []
    pozicija = 1
    for data in dict_tabele:
        recnik_rezultata_tima = {"position": pozicija, "team": data[8], "matches": {"played": data[0],
                                 "won": data[1], "draw": data[2], "lose": data[3]}, "scores": {"for":
                                 data[4], "against": data[5], "goal difference": data[6]}, "points": data[8]
                                 }
        tabela_timova_i_njihovih_rezultata.append(recnik_rezultata_tima)
        pozicija += 1
    return tabela_timova_i_njihovih_rezultata


engleska_liga = football.pravljenje_dobijenih_rezultata_dict(tabela)
print(engleska_liga)

english_league = 'english_final_table_2018.json'
with open(english_league, 'w') as file:
    json.dump(engleska_liga, file)


# def odstampaj_tabelu(lista_rezultata):
#     text = ["Position", "Team", "Played", "Won", "Draw", "Lose", "For", "Against", "GD", "Points"]
#     print(text[0].ljust(12, " "), text[1].ljust(22, " "), text[2].ljust(8, " "), text[3].ljust(5, " "),
#           text[4].ljust(8, " "), text[5].ljust(8, " "), text[6].ljust(6, " "), text[7].ljust(8, " "),
#           text[8].ljust(5, " "), text[9].ljust(5, " "))
#     for index in range(0, len(lista_rezultata)):
#         print(
#             str(index + 1).ljust(12, " ") + str(lista_rezultata[index][8]).ljust(25, " ") + str(
#                 lista_rezultata[index][0]).ljust(8, " ") +
#             str(lista_rezultata[index][1]).ljust(8, " ") + str(lista_rezultata[index][2]).ljust(8, " ") + str(
#                 lista_rezultata[index][3]).ljust(8, " ") +
#             str(lista_rezultata[index][4]).ljust(8, " ") + str(lista_rezultata[index][5]).ljust(8, " ") + str(
#                 lista_rezultata[index][6]).ljust(8, " ") +
#             str(lista_rezultata[index][7]).ljust(8, " "))
#
#
# odstampaj_tabelu(tabela)
#


