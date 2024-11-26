broj = int(input())

rec = list(input())

samoglasnici = ['a', 'e', 'i', 'o', 'u']

resenje = len(list(filter(lambda x: x in samoglasnici, rec)))

print(broj - resenje)