lista = [1, 3, 4, 5, 9]


def remove(elements, remove_element):
    if remove_element not in elements:
        raise Exception

    return discard(elements, remove_element)


def anotherRemove(elements, remove_element):
    collection = discard(elements, remove_element)
    if len(collection) == len(elements):
        raise Exception

    return collection


def discard(elements, discard_element):
    lista_sa_obrisanim_elementima = []
    if discard_element in elements:
        index = 0
        for pozicija in elements:
            if discard_element == pozicija:
                break
            else:
                index = index + 1
        elements[0], elements[index] = elements[index], elements[0]
        for x in range(1, len(elements)):
            if len(elements) > 1:
                sacuvani_element = elements.pop()
                lista_sa_obrisanim_elementima.append(sacuvani_element)
        return lista_sa_obrisanim_elementima
    else:
        return elements


def remove_without_pop(elements, remove_elemement):
    remove_lista = []
    if remove_elemement in elements:
        for sacuvani_element in elements:
            if remove_elemement == sacuvani_element:
                continue
            else:
                remove_lista.append(sacuvani_element)
        return remove_lista
    else:
        raise Exception


pokretanje_discard = discard(lista, 1)
print(pokretanje_discard)
lista = [1, 3, 4, 5, 9]
pokretanje_remove = remove_without_pop(lista, 4)
print(pokretanje_remove)
