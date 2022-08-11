import json

all_categories = 'all_categories.json'


def sort_category_by_rate_desc(categories):  # 4.0 : 4.1 >
    for index in range(0, len(categories) - 1):
        if categories[index]['rate'] < categories[index + 1]['rate']:
            categories[index], categories[index + 1] = categories[index + 1], categories[index]
    return categories


def write_json_file(list, file):
    with open(file, 'w') as outfile:
        json.dump(list, outfile)

name = property()
def sort_category_by_rate_asc(categories):
    for index in range(0, len(categories) - 1):
        if categories[index]['rate'] > categories[index + 1]['rate']:
            categories[index], categories[index + 1] = categories[index + 1], categories[index]
    return categories


def get_all_categories_greather_than_rate(categories, rate):  # data
    filtered_list = []  # nova_lista
    for category in categories:  # data sluzi za prolaz
        if category['rating']['rate'] >= rate:
            title_key = 'title'
            category_key = 'category'
            rate_key = 'rate'

            short_category = {title_key: category[title_key], category_key: category[category_key],
                              rate_key: category['rating'][rate_key]}
            filtered_list.append(short_category)  # u novu listu ubacujem elemente koji zadovoljavaju kriterijum

    sorted_list_desc = sort_category_by_rate_asc(
        filtered_list)  # u listu za sortiranjem prosledjujem novu listu a ne data
    for broj_ponavljanja in range(0, len(categories)):
        sorted_list_desc = sort_category_by_rate_desc(filtered_list)
    return sorted_list_desc


def get_all_categories_less_than_rate(categories, rate):
    filtered_list = []
    for category in categories:
        if category['rating']['rate'] <= rate:
            title_key = 'title'
            category_key = 'category'
            rate_key = 'rate'

            short_category = {title_key: category[title_key], category_key: category[category_key],
                              rate_key: category['rating'][rate_key]}
            filtered_list.append(short_category)

    sorted_list_asc = sort_category_by_rate_asc(filtered_list)
    for broj_ponavljanja in range(0, len(categories)):
        sorted_list_asc = sort_category_by_rate_asc(filtered_list)
    return sorted_list_asc


def get_all_categories_equals_by_rate(categories, rate):
    filtered_list = []
    for category in categories:
        if category['rating']['rate'] == rate:
            title_key = 'title'
            category_key = 'category'
            rate_key = 'rate'

            short_category = {title_key: category[title_key], category_key: category[category_key],
                              rate_key: category['rating'][rate_key]}
            filtered_list.append(short_category)

    sorted_list_desc = sort_category_by_rate_asc(filtered_list)
    for broj_ponavljanja in range(0, len(categories)):
        sorted_list_desc = sort_category_by_rate_desc(filtered_list)
    return sorted_list_desc


def get_all_categories_between_two_rate(categories, min_rate, max_rate):
    filtered_list = []
    for category in categories:
        if category['rating']['rate'] >= min_rate and category['rating']['rate'] <= max_rate:
            title_key = 'title'
            category_key = 'category'
            rate_key = 'rate'

            short_category = {title_key: category[title_key], category_key: category[category_key],
                              rate_key: category['rating'][rate_key]}
            filtered_list.append(short_category)

    sorted_list_desc = sort_category_by_rate_asc(filtered_list)
    for broj_ponavljanja in range(0, len(categories)):
        sorted_list_desc = sort_category_by_rate_desc(filtered_list)
    return sorted_list_desc


with open(all_categories, 'r') as file:
    data = json.load(file)
    for item in data:
        print(item['rating']['rate'])
    categories_greather = get_all_categories_greather_than_rate(data, 4.0)
    write_json_file(categories_greather, 'categories_greather_than.json')
    print(categories_greather)
    categories_less = get_all_categories_less_than_rate(data, 4.0)
    write_json_file(categories_less, 'categories_less_than.json')
    print(categories_less)
    categories_equal = get_all_categories_equals_by_rate(data, 4.8)
    print(categories_equal)
    categories_between = get_all_categories_between_two_rate(data, 3.0, 3.9)
    print(categories_between)


# TODO: create def that you can filter categories by rate (ex. rate greater than, less than, equals and between)
# TODO: write returned value in categories_greather_than.json, categories_less_than.json, categories_equals.json and categories_between.json
#  text files only data of title, category and rate
