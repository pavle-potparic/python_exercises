def remove (elements, remove_element):
    if remove_element not in elements:
        raise Exception

    collection = []
    for element in elements:
        if element == remove_element:
            pass
        else:
            collection.append(elements)

    return collection


def discard(elements, discard_element):
    collection = []
    for element in elements:
        if element == discard_element:
            pass
        else:
            collection.append(elements)

    return collection
