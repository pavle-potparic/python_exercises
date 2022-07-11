input_filename = 'country_info.txt'
dict_drzava = {}
countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    drzava = input("Napisi neku drzavu.")
    drzava = drzava.casefold()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        zip(capital, country)


        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict


# print(countries)
print(countries)



