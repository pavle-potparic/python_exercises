import json


def get_data(file):
    with open(file, "r", encoding="utf-8") as stream:
        data = json.load(stream)
        return data


def get_from_dict_by_key(dict_of_all_teams, team):
    '''
    Function must return dictionary team.
    :param dict_of_all_teams: is a dictionary of with all data about clubs in english league
    :param team: is a dict with value: clubs in english league
    :return: function return :param team
    '''
    return dict_of_all_teams[team]


def get_name_of_teams(all_clubs, key):
    '''
    Function must return list full of names of teams
    :param all_clubs: is :param team in prev function
    :param key: is a value: name in :param all_clubs
    :return: list full of names of clubs
    '''
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
    '''
    Function must return changed match_list to list
    :param match_list: is a dict with datas of all matches in season
    :return: list of :param match_list
    '''
    list_of_matches = []
    for match in match_list:
        list_of_matches.append(match['matches'])
    return list_of_matches


def get_points_of_one_team(list_of_matches, list_of_results, team_names):
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
    '''
    :param dict_timova_i_njihovih_rezultata: is a dictionary with results of all teams which must be changed in a list
    :return: list with results of all teams in the row
    '''
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


def pravljenje_dobijenih_rezultata_dict(dict_tabele):
    tabela_timova_i_njihovih_rezultata = []
    pozicija = 1
    for data in dict_tabele:
        recnik_rezultata_tima = {"position": pozicija, "team": data[8], "matches": {"played": data[0],
                                                                                    "won": data[1], "draw": data[2],
                                                                                    "lose": data[3]}, "scores": {"for":
                                                                                                                     data[
                                                                                                                         4],
                                                                                                                 "against":
                                                                                                                     data[
                                                                                                                         5],
                                                                                                                 "goal difference":
                                                                                                                     data[
                                                                                                                         6]},
                                 "points": data[7]
                                 }
        tabela_timova_i_njihovih_rezultata.append(recnik_rezultata_tima)
        pozicija += 1
    return tabela_timova_i_njihovih_rezultata


def write_to_file(file_to_write: str, final_table: list) -> None:
    """
    Write final table of football league sorted by position in json format.

    :param file_to_write: Name of file to write final table in
    :param final_table: List of final table with all data sorted by position (mathces, scores, position). List contains nested dictionary with data.
    :return: None
    """

    with open(file_to_write, 'w') as file:
        json.dump(final_table, file)


def write_final_table(teams, matches, file):
    data_teams = get_data(teams)
    all_clubs = get_from_dict_by_key(data_teams, "clubs")
    team_names = get_name_of_teams(all_clubs, 'name')
    prepare_teams_dict = prepare_teams_score_dict(team_names)

    data_matches = get_data(matches)
    match_rounds = get_from_dict_by_key(data_matches, "rounds")
    list_of_matches = get_list_of_matches(match_rounds)

    timovi_i_nihovi_rezultati = get_points_of_one_team(list_of_matches, prepare_teams_dict, team_names)
    tabela = pravljenje_tabele(timovi_i_nihovi_rezultati)


    table_of_league = pravljenje_dobijenih_rezultata_dict(tabela)
    print(table_of_league)

    write_to_file(file, table_of_league)