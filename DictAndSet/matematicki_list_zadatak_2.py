nivoi = int(input("Unesi broj nivoa."))
podnivoi = int(input("Unesi broj podnivoa u jednom nivou."))
lista_nivoa = []
index_nivoa = 0
lista_pokusaja = [155, 130, 92, 115, 140, 146, 148]
# 1 2 100 2 2 120 2 4 200 3 1 140
# while index_nivoa < nivoi:
#    index_podnivoa = 0
#    lista_podnivoa = []
#    while index_podnivoa < podnivoi:
#        lista_podnivoa.append(0)
#        index_podnivoa += 1
#    lista_nivoa.append(lista_podnivoa)
#   index_nivoa += 1


broj_teskih_nivoa = int(input("Unesi broj teskih nivoa."))
broj = 0
lista_teskih_nivoa = []
while broj != broj_teskih_nivoa:
    teski_nivoi = input('Unesi teski nivo')
    tezak_nivo = teski_nivoi.split(" ")
    lista_teskih_nivoa.append(tezak_nivo)
    broj = broj + 1
    print(lista_teskih_nivoa)

pokusaj = 0

poeni = 0
# for sabiranje_rezultata in lista_teskih_nivoa:
#     da_li_je_presao_nivo = True
#     index = 0
#     for element in sabiranje_rezultata:
#         element = int(element)
#         if index == 3:
#             if sabiranje_rezultata[2] >= int(lista_pokusaja[pokusaj]):
#                 poeni = poeni + 10
#                 pokusaj = pokusaj + 1
#             else:
#                 da_li_je_presao_nivo = False
#                 pokusaj = pokusaj + 1
#                 poeni = poeni + 5
#                 break
#
#         index = index + 1
#     if da_li_je_presao_nivo:
#         poeni = poeni + (podnivoi - 1) * 5
#     else:
#         poeni = poeni + (int(sabiranje_rezultata[0]) - 1) * 5


# print(poeni)
# for teski_nivo in lista_teskih_nivoa:
#    nivo = int(teski_nivo[0]) - 1
#    podnivo = int(teski_nivo[1]) - 1
#    lista_nivoa[nivo][podnivo] = int(teski_nivo[2])

# print(lista_nivoa)

trenutni_nivo = 1
da_li_je_predjen_prethodni_nivo = True
index = 0

for teski_nivo in lista_teskih_nivoa:
    nivo = int(teski_nivo[0])
    podnivo = int(teski_nivo[1])
    vreme = int(teski_nivo[2])

    while trenutni_nivo < nivo:
        for pokusaj in range(index, podnivoi):
            lista_pokusaja.remove(lista_pokusaja[0])
            poeni += 5
        trenutni_nivo += 1
        index = 0

    if trenutni_nivo > nivoi:
        break
    elif trenutni_nivo == nivo:
        prolazno_vreme = lista_pokusaja[podnivo - 1]
        if prolazno_vreme <= vreme:
            da_li_je_predjen_prethodni_nivo = True
            poeni += 5
            index = podnivo
        else:
            da_li_je_predjen_prethodni_nivo = False
            trenutni_nivo += 1
            index = 0
        for pokusaj in range(0, podnivo):
            lista_pokusaja.remove(lista_pokusaja[0])
            poeni += 5

print(poeni)
print(lista_pokusaja)
