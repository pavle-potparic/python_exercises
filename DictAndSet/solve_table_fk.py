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
    lista_gol_razlike = []
    for key, value in league.items():
        total_score = 0
        for score in value:
            if score == value[0]:
                total_score = score * 3
            if score == value[1]:
                total_score = total_score + score
        lista_timova.append(key)
        lista_bodova.append(total_score)
        lista_gol_razlike.append(value[3] - value[4])

    total_score_dict = dict(zip(lista_timova, lista_bodova))
    pozicija = sorted(total_score_dict.items(), key=lambda x: x[1], reverse=True)
    lista_lige = list(pozicija)
    pocetak_drugog_for = 0
    menjanje_mesta = 1
    for isti_rezultat in lista_lige:
        pocetak_drugog_for = pocetak_drugog_for + 1
        menjanje_mesta = menjanje_mesta + 1
        if pocetak_drugog_for > 1:
            for isti_rezultat1 in lista_lige:
                if isti_rezultat == isti_rezultat1:
                    if lista_gol_razlike[pocetak_drugog_for - 2] < lista_gol_razlike[menjanje_mesta - 2]:
                        lista_lige[pocetak_drugog_for[0]], lista_lige[
                            menjanje_mesta[0]] = lista_lige[menjanje_mesta][0], lista_lige[pocetak_drugog_for][0]

    print(lista_lige)


table_of_league(english_league)
