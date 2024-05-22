duzina_stana = int(input())
sirina_stana = int(input())

duzina_stuba = int(input())
sirina_stuba = int(input())

levo_udaljenost = int(input())
dole_udaljenost = int(input())

if levo_udaljenost > duzina_stana - duzina_stuba - levo_udaljenost:
    print(duzina_stana - duzina_stuba - levo_udaljenost, end=' ')

else:
    print(levo_udaljenost, end=' ')

if dole_udaljenost > sirina_stana - sirina_stuba - dole_udaljenost:
    print(sirina_stana - sirina_stuba - dole_udaljenost)

else:
    print(dole_udaljenost)