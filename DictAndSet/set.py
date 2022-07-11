from primes_and_squares import slicnosti_i_razlike


# Napraviti fajl primes_and_squares i u njemu napraviti dve metode
# jedna vraca sve proste brojeve do zadatog broja
# druga vraca sve kvadratne brojeve do zadatog broja

# pronadji: uniju, razliku, presek, simetricnu uniju
# napravi posebnu promenljivu koja ce da izvrsi update sa prostim
# napravi razlicite promenljive koje ce da izvrse razlicite vrste update-a (update.intersection itd)

#Subset and superset
animals = ['Bear', 'Tiger', 'Lion', 'Wolf', 'Dog', 'Eagle', 'Hawk']
wild_cat = ['Tiger', 'Lion']

print(set(animals).issuperset(wild_cat))
print(set(wild_cat).issubset(animals))

#is subset
print(set(wild_cat) <= set(wild_cat))
#is proper subset
print(set(wild_cat) < set(wild_cat))

# moja_lista = ['ime', 'prezime', 'nadimak']
# moj_set = set(moja_lista)
# print(moj_set)
# moj_set.add(moja_lista)
# print(moj_set)

frozen_animals = frozenset(animals)
print(frozen_animals)