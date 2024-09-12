prva_rec = input()
druga_rec = input()
resenje = "da"

if len(druga_rec) < len(prva_rec):
    for x in prva_rec:
        if x in druga_rec:
            pass
        else:
            resenje = "ne"

else:
    for x in druga_rec:
        if x in prva_rec:
            pass
        else:
            resenje = "ne"

print(resenje)