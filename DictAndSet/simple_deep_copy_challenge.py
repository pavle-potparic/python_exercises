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
        lista_vrednosti = []
        for deep_kljuc, deep_vrednost in vrednost.items():
            lista_vrednosti.append(deep_vrednost)
        secondary_dict = dict(zip(vrednost.keys(), lista_vrednosti))
        nova_lista.append(secondary_dict)

    d_copy = dict(zip(d.keys(), nova_lista))

    return d_copy


recipes_copy = my_deep_copy(recipes)
# recipes_copy = recipes.copy()
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
# print(recipes)
print(recipes["Butter chicken"]["ginger"])
