x, y = list(map(int, input().split(" ")))
z, q = list(map(int, input().split(" ")))
vertikala = int(input())
lista_vertikala = input()
lista_vertikala = lista_vertikala.rstrip()
lista_vertikala = list(map(int, lista_vertikala.split(" ")))
horizontala = int(input())
lista_horizontala = input()
lista_horizontala = lista_horizontala.rstrip()
lista_horizontala = list(map(int, lista_horizontala.split(" ")))

if x > z:
    resenje1 = list(filter(lambda i: z <= i <= x, lista_vertikala))

else:
    resenje1 = list(filter(lambda i: x <= i <= z, lista_vertikala))

if y > q:
    resenje2 = list(filter(lambda i: q <= i <= y, lista_horizontala))

else:
    resenje2 = list(filter(lambda i: y <= i <= q, lista_horizontala))

print(len(resenje1) + len(resenje2))
