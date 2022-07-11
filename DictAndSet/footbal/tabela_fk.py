def table_of_league(league: dict):
    """
    Function for creating table of league, order by position (the most points in league). All win counts three points, draw counts one point.
    If some of team has equal total points, team with better goal difference are on better position then other.
    :param league: League has all teams, their `names` are the `key`, and `value` is list of data
    (`win`, `draw`, `lose`, `number of scored goals`, `number of conceded goals`)
    :return: dictionary ordered by total points and position of each team
    """
    lista_timova = []
    lista_bodova = []
    for key, value in league.items():
        total_score = 0
        for score in value:
            if score == value[0]:
                total_score = score * 3
            if score == value[1]:
                total_score = total_score + score
        lista_timova.append(key)
        lista_bodova.append(total_score)

    total_score_dict = dict(zip(lista_timova, lista_bodova))
    pozicija = sorted(total_score_dict.items(), key=lambda x: x[1], reverse=True)

    for stampanje, stampanje2 in pozicija:
        print(stampanje, stampanje2)


def add_column_goal_different(teams: dict) -> None:
    """

    :param teams: dict that represent all teams in league with data
    :return: None
    """
    for key, value in teams.items():
        goal_diff = value[3] - value[4]
        value.append(goal_diff)


def add_column_total_points(teams: dict) -> None:
    """
    Adding new column in dictionary of league. This column contains total score. It counted by first and second element
     in list of data that we can find in dict value (`value[0]` and `value[1]`). First element multiply by 3 because
     it is number of wins, and second element counted by one because it is number of draws.
    :param teams: dict that represent all teams in league with data
    :return: None
    """
    for key, value in teams.items():
        points_for_wins = value[0] * 3
        points_for_draws = value[1]
        total_score = points_for_wins + points_for_draws
        value.append(total_score)


def convert_dict_to_list(teams: dict) -> list:
    """
    Converting dict of teams to list. Last element is name of team. We append it from key of dict.
    :param teams: dict that represent all teams in league with data
    :return: list of teams with all data include name of teams as last element
    """
    list_of_teams = []
    for key, value in teams.items():
        value.append(key)
        list_of_teams.append(value)

    return list_of_teams


def sort_list_of_teams(list_of_teams: list) -> None:
    """

    :param teams: list_of_teams that contains all teams in league with data
    :return: None
    """

    points_position = 6
    goal_diff_position = 5
    goal_scores_position = 3

    for team_position in range(0, len(list_of_teams) - 1):
        for comparing_team_position in range(team_position + 1, len(list_of_teams)):
            temp = list_of_teams[team_position]
            if (list_of_teams[team_position][points_position] < list_of_teams[comparing_team_position][
                points_position]):
                list_of_teams[team_position] = list_of_teams[comparing_team_position]
                list_of_teams[comparing_team_position] = temp
            elif (list_of_teams[team_position][points_position] == list_of_teams[comparing_team_position][
                points_position]):
                if (list_of_teams[team_position][goal_diff_position] < list_of_teams[comparing_team_position][
                    goal_diff_position]):
                    list_of_teams[team_position] = list_of_teams[comparing_team_position]
                    list_of_teams[comparing_team_position] = temp
                elif (list_of_teams[team_position][goal_diff_position] == list_of_teams[comparing_team_position][
                    goal_diff_position]):
                    if (list_of_teams[team_position][goal_scores_position] < list_of_teams[comparing_team_position][
                        goal_scores_position]):
                        list_of_teams[team_position] = list_of_teams[comparing_team_position]
                        list_of_teams[comparing_team_position] = temp


def convert_list_to_dictionary(list_of_teams: list) -> dict:
    """
    Convert list to the dictionary.
    :param list_of_teams: is a list of the all teams.
    :return: return converted dictionary from list_of_teams .
    """
    dictionary_of_teams = {}
    for key in range(0, len(list_of_teams)):
        name_of_team = list_of_teams[key][7]
        dictionary_of_teams[name_of_team] = list_of_teams[key]
        list_of_teams[key].pop(7)

    return dictionary_of_teams


def prepare_finally_table(teams: dict) -> dict:
    """
    This function calls all function that added new column of goal different, sorted all data and convert list to dict
    and dict to list.
    :param teams: Team is a parameter of english league.
    :return: return all functions
    """
    add_column_goal_different(teams)

    add_column_total_points(teams)

    list_of_all_teams = convert_dict_to_list(teams)

    sort_list_of_teams(list_of_all_teams)

    sorted_dict = convert_list_to_dictionary(list_of_all_teams)

    return sorted_dict


def print_table(teams: dict) -> None:
    """
    Print dictionary and lists in this dictionary. The challenge is that everything has to be on the same level.
    :param teams: Team is a parameter of english league.
    :return: None
    """
    # "Position Team Played Won Draw Lose For Against Goal-diff Points"
    text = ["Position", "Team", "Played", "Won", "Draw", "Lose", "For", "Against", "GD", "Points"]
    print(text[0].ljust(12, " "), text[1].ljust(22, " "), text[2].ljust(8, " "), text[3].ljust(5, " "),
          text[4].ljust(8, " "), text[5].ljust(8, " "), text[6].ljust(6, " "), text[7].ljust(8, " "),
          text[8].ljust(5, " "), text[9].ljust(5, " "))
    position = 0
    for team_name, team_data in teams.items():
        position = position + 1
        won = team_data[0]
        draw = team_data[1]
        lose = team_data[2]
        played_game = won + draw + lose
        scored_goal = team_data[3]
        against = team_data[4]
        goal_diff = team_data[5]
        total_points = team_data[6]
        position_column = str(position) + "."
        print(str(position_column).ljust(12, " ") + str(team_name).ljust(25, " ") + str(played_game).ljust(8, " ") +
              str(won).ljust(8, " ") + str(draw).ljust(8, " ") + str(lose).ljust(8, " ") +
              str(scored_goal).ljust(8, " ") + str(against).ljust(8, " ") + str(goal_diff).ljust(8, " ") +
              str(total_points).ljust(8, " "))


english_league = {"Chelsea": [11, 2, 7, 43, 27],
                  "Manchester City": [7, 11, 2, 36, 22],
                  "Arsenal": [10, 1, 9, 36, 32],
                  "Tottenham": [9, 9, 2, 37, 33],
                  "Manchester United": [8, 6, 6, 35, 34],
                  "Newcastle": [7, 3, 10, 43, 27],
                  "Aston vila": [4, 6, 10, 22, 32],
                  "Blackburn": [5, 4, 11, 25, 32],
                  "Fulham": [6, 8, 6, 31, 35],
                  "Liverpool": [10, 1, 9, 41, 31],
                  "Lester": [8, 3, 9, 27, 34],
                  "Southampton": [6, 5, 9, 22, 31],
                  "Coventry": [5, 9, 6, 23, 36],
                  "Sunderland": [5, 8, 7, 28, 31], }

finally_table = prepare_finally_table(english_league)
print_table(finally_table)
# print(english_league)


# Position    Team          Played  Won     Draw    Lose    For     Against   Goal-diff   Points
# 1.          Tottenham     20      9       9       2       37      33        4           36
# lista = [[45, 55, 66, 77], [11, 15, 43, 22]]
