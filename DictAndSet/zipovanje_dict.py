prva_lista = [1, 2, 3, 4, 5]
druga_lista = ["jedan", "dva", "tri"]

dict_zip = dict(zip(druga_lista, prva_lista))

# dict_zip_dva = dict(zip(prva_lista, 4))  ovo ne moze

dict_zip_tri = dict(zip("Jelena", [1, 2, 3]))
print(dict_zip_tri)
