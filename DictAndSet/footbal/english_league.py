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
all_clubs = football.get_from_dict_by_key(data_teams, "clubs")
team_names = football.get_name_of_teams(all_clubs, 'name')
prepare_teams_dict = football.prepare_teams_score_dict(team_names)

data_matches = football.get_data(english_matches)
match_rounds = football.get_from_dict_by_key(data_matches, "rounds")
list_of_matches = get_list_of_matches(match_rounds)

timovi_i_nihovi_rezultati = get_points_of_one_team(list_of_matches, prepare_teams_dict)
tabela = pravljenje_tabele(timovi_i_nihovi_rezultati)

english_league = football.pravljenje_dobijenih_rezultata_dict(tabela)
print(english_league)


english_league = 'english_final_table_2018.json'
with open(english_league, 'w') as file:
    json.dump(english_league, file)
