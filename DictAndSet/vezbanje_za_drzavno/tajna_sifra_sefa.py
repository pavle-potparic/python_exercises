broj = int(input())

lista = list(map(int, input().split(" ")))
resenje = broj - lista.index(min(lista))

print(resenje)


rec = input()
rec = rec.lower()
print(rec)

print(rec.count("a"))
print(rec.index("a"))