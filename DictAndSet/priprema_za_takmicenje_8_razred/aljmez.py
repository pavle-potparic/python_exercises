broj = int(input())
lista = []

for x in range(0, broj):
    y, masa = list(map(float, input().split(" ")))
    x_osa = 126 / masa
    if y < 0 and x_osa < 0:
        lista.append([x+1, y, 126 / masa, x_osa-abs(y)])
    else:
        lista.append([x+1, y, 126 / masa, x_osa+abs(y)])

lista.sort(key=lambda z: z[3], reverse=True)

print(*[podlista[0] for podlista in lista])
print(lista)