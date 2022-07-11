from contents import recipes


def my_deep_copy(d: dict) -> dict:
    """Copy a dictionary, creating copies of the `list` or `dict` values.

    The function will crash with an AttributeError if the values aren't
    list or dictionaries.

    :param d: The dictionary to copy.
    :return: A copy of `d`, with the values being copies of the original values.
    """

    nova_lista = []

    for kljuc, vrednost in d.items():
        lista_elemenata = []

        for vrednost_kljuc, vrednost_vrednost in vrednost.items():
            lista_elemenata.append(vrednost_vrednost)

        dict_of_element = dict(zip(vrednost.keys(), lista_elemenata))
        nova_lista.append(dict_of_element)

    return dict(zip(d.keys(), nova_lista))


recipes_copy = my_deep_copy(recipes)
# recipes_copy = recipes.copy()
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
