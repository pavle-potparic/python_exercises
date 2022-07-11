input_filename = 'country_info.txt'
countries = {}
cities = {}

with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        zip(capital, country)

        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }

        countries[country.casefold()] = country_dict
        cities[capital.casefold()] = country_dict


def getCapitalOfCountry(dict_counties, country):
    try:
        return dict_counties.get(country.casefold()).get('capital')
    except:
        return None


def getCountryOfCapital(dict_cities, capital):
    try:
        return dict_cities.get(capital.casefold()).get('name')
    except:
        return None


def getDataFromDict(dict, key, column):
    try:
        return dict.get(key.casefold()).get(column)
    except:
        return None


def getCurrencyFromCountry(dict_country, country):
    return getDataFromDict(dict_country, country, 'currency')



# city = getCapitalOfCountry(countries, 'Serbia')
# country = getCountryOfCapital(cities, 'Belgrade')

city = getDataFromDict(countries, 'Serbia', 'currency')
country = getDataFromDict(cities, 'Belgrade', 'name')

valute = getCurrencyFromCountry(countries, 'Serbia')

print(city)
print(country)
print(valute)
