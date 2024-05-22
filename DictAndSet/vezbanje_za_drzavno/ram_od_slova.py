rec = input()

print(rec)
tacke = '.' * (len(rec) - 2)
counter = 2
for x in range(1, len(rec)-1):
    print(rec[x] + tacke + rec[-counter])
    counter += 1

print(rec[::-1])