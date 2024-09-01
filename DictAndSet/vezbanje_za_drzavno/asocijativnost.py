n = int(input())

lista = []

for x in range(0, n):
    lista.append(list(map(int, input().split(" "))))

prvi = lista[0][0]
drugi = lista[0][1]

if prvi - drugi == lista[prvi][drugi] or prvi + drugi == lista[prvi][drugi] or prvi / drugi == lista[prvi][drugi] or prvi * drugi == lista[prvi][drugi]:
    print("da")

else:
    print("ne")