import json

def get_data(file):
    with open(file, "r", encoding="utf-8") as stream:
        data = json.load(stream)
        return data

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



